package nu.datex2.demo.configuration;

import nu.datex2.situation.invoker.ApiClient;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class ApiClientConfiguration {

    @Bean
    public ApiClient apiClient() {
        return new ApiClient();
    }
}
