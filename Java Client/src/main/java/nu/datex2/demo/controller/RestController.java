package nu.datex2.demo.controller;

import nu.datex2.demo.service.DatexPublicPullService;
import org.geojson.FeatureCollection;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;

@org.springframework.web.bind.annotation.RestController
public class RestController {

    private final DatexPublicPullService service;

    public RestController(DatexPublicPullService service) {
        this.service = service;
    }

    @GetMapping("feature-collection")
    public ResponseEntity<FeatureCollection> get() {
        var featureCollection = new FeatureCollection();
        featureCollection.setFeatures(service.getFeatures());
        return ResponseEntity.ok(featureCollection);
    }
}
