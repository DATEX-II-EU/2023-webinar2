package nu.datex2.demo.service;

import jakarta.annotation.PostConstruct;
import nu.datex2.situation.api.DevelopersApi;
import nu.datex2.situation.invoker.ApiClient;
import nu.datex2.situation.model.Accident;
import nu.datex2.situation.model.LocationReferenceG;
import nu.datex2.situation.model.MessageContainer;
import nu.datex2.situation.model.Situation;
import org.geojson.Feature;
import org.geojson.GeoJsonObject;
import org.geojson.LngLatAlt;
import org.geojson.Point;
import org.springframework.stereotype.Service;

import java.time.Instant;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

@Service
public class DatexPublicPullService {

    private final ApiClient apiClient;

    public DatexPublicPullService(ApiClient apiClient) {
        this.apiClient = apiClient;
    }

    private List<Feature> features = new ArrayList<>();

    public List<Feature> getFeatures() {
        return features;
    }

    @PostConstruct
    public void pullData() {
        var developersApi = new DevelopersApi(apiClient);

        MessageContainer messageContainer = developersApi.pullsnapshotdata().block();

        var payload = messageContainer.getPayload().get(0);

        List<Feature> features = new ArrayList<>();
        var exchangeInformation = messageContainer.getExchangeInformation();
        var exchangeProtocol = exchangeInformation.getExchangeContext().getCodedExchangeProtocol().getValue().getValue();
        var messageContainerCreationTime = exchangeInformation.getDynamicInformation().getMessageGenerationTimestamp();

        for (var situation : payload.getSituationSituationPublication().getSituation()) {
            features.addAll(mapSituation(situation, exchangeProtocol, messageContainerCreationTime));
        }

        this.features = features;
    }

    private List<Feature> mapSituation(Situation situation, String exchangeProtocol, Instant messageContainerCreationTime) {
        List<Feature> features = new ArrayList<>();

        for (var sitRecord : situation.getSituationRecord()) {
            var sitRecordAccident = sitRecord.getSituationAccident();

            var feature = new Feature();
            feature.setId(sitRecordAccident.getIdG());
            feature.setProperties(buildFeatureProperties(sitRecordAccident));
            feature.setProperty("exchangeProtocol", exchangeProtocol);
            feature.setProperty("messageContainerCreationTime", messageContainerCreationTime);

            var location = sitRecordAccident.getLocationReference();
            feature.setGeometry(geometry(location));

            features.add(feature);
        }

        return features;
    }

    private HashMap<String, Object> buildFeatureProperties(Accident sitRecordAccident) {
        HashMap<String, Object> properties = new HashMap<>();

        properties.put("id", sitRecordAccident.getIdG());
        properties.put("version", sitRecordAccident.getVersionG());
        properties.put("situationRecordCreationTime", sitRecordAccident.getSituationRecordCreationTime());
        properties.put("situationRecordVersionTime", sitRecordAccident.getSituationRecordVersionTime());
        properties.put("validityStatus", sitRecordAccident.getValidity().getValidityStatus().getValue());
        properties.put("overallStartTime", sitRecordAccident.getValidity().getValidityTimeSpecification().getOverallStartTime());
        properties.put("overallEndTime", sitRecordAccident.getValidity().getValidityTimeSpecification().getOverallEndTime());
        properties.put("probabilityOfOccurrence", sitRecordAccident.getProbabilityOfOccurrence().getValue());
        properties.put("accidentType", sitRecordAccident.getAccidentType().get(0).getValue());
        properties.put("collisionType", sitRecordAccident.getCollisionType().getValue().getValue());

        return properties;
    }

    private GeoJsonObject geometry(LocationReferenceG location) {
        if (location.getLocationReferencingPointLocation() != null) {
            var pointLocation = location.getLocationReferencingPointLocation();
            return new Point(new LngLatAlt(
                    pointLocation.getPointByCoordinates().getPointCoordinates().getLongitude().doubleValue(),
                    pointLocation.getPointByCoordinates().getPointCoordinates().getLatitude().doubleValue()
            ));
        } else {
            throw new RuntimeException("Location type currently not supported");
        }
    }
}
