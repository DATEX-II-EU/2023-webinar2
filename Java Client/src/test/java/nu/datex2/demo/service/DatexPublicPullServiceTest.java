package nu.datex2.demo.service;

import com.github.tomakehurst.wiremock.WireMockServer;
import com.github.tomakehurst.wiremock.core.WireMockConfiguration;
import nu.datex2.situation.invoker.ApiClient;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.core.io.ClassPathResource;

import java.io.IOException;
import java.io.InputStream;

import static com.github.tomakehurst.wiremock.client.WireMock.configureFor;
import static com.github.tomakehurst.wiremock.client.WireMock.get;
import static com.github.tomakehurst.wiremock.client.WireMock.ok;
import static com.github.tomakehurst.wiremock.client.WireMock.stubFor;
import static org.assertj.core.api.Assertions.assertThat;

public class DatexPublicPullServiceTest {

    private WireMockServer mockServer;

    private DatexPublicPullService service;

    @BeforeEach
    void setup() {
        // Start wiremock server
        mockServer = new WireMockServer(new WireMockConfiguration().dynamicPort());
        mockServer.start();
        configureFor(mockServer.port());
        var endpoint = "http://localhost:" + mockServer.port();

        // Create mock ApiClient configuration
        var apiClient = new ApiClient();
        apiClient.setBasePath(endpoint);

        // Create service instance
        service = new DatexPublicPullService(apiClient);
    }

    @AfterEach
    void cleanup() {
        if (mockServer != null) {
            mockServer.stop();
        }
    }

    @Test
    void verifyFetchingOfSnapshotAndConversionToGeojson() throws Exception {
        // Given
        givenMockWebServerWillReturnSnapshot();

        // When
        service.pullData();

        // Then
        var feature = service.getFeatures().get(0);
        var testFeature = TestConstants.feature();
        assertThat(feature.getId()).contains(testFeature.getId());
    }

    private void givenMockWebServerWillReturnSnapshot() throws Exception {
        stubFor(get("/pullsnapshotdata").willReturn(ok().withBody(inputStream("pull-snapshot.json").readAllBytes()).withHeader("Content-Type", "application/json")));
    }

    private InputStream inputStream(String file) throws IOException {
        var resource = new ClassPathResource(file);

        return resource.getInputStream();
    }
}
