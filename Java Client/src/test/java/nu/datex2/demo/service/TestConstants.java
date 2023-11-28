package nu.datex2.demo.service;

import org.geojson.Feature;
import org.geojson.LngLatAlt;
import org.geojson.Point;

public class TestConstants {

    public static Feature feature() {
        var feature = new Feature();
        feature.setId("d867af14-4a5d-4015-8925-f3f37033ff87");
        feature.setProperty("probabilityOfOccurrence", "certain");
        feature.setProperty("situationRecordCreationTime", "2023-11-12T14:01:27.838004700Z");
        feature.setProperty("overallEndTime", "2023-11-12T16:01:27.838435600Z");
        feature.setProperty("overallStartTime", "2023-11-12T14:01:27.838396900Z");
        feature.setProperty("situationRecordVersionTime", "2023-11-12T14:01:27.838044600Z");
        feature.setProperty("validityStatus", "active");
        feature.setProperty("accidentType", "accident");
        feature.setProperty("id", "d867af14-4a5d-4015-8925-f3f37033ff86");
        feature.setProperty("collisionType", "collisionWithAnimal");
        feature.setProperty("version", "1");

        var pointGeometry = new Point(new LngLatAlt(5.204404542910014,53.01894771995707));
        feature.setGeometry(pointGeometry);

        return feature;
    }
}
