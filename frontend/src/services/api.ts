import axios from "axios";
import TokenService  from "./token.service";

const instance = axios.create({
    baseURL: 'http://localhost:8002/api',
    headers: {
        'Content-Type': 'application/json'
    }
});

instance.interceptors.request.use(
    async (config) => {
        if(!config.headers) return config;

        if(config.url !== '/login') {
            if (config.url === '/refresh') {
                config.headers['Authorization'] = `Bearer ${TokenService.getRefreshToken()}`;
            } else if (config.url === '/logout') {
                const refreshToken = TokenService.getRefreshToken();

                if (refreshToken) {
                    config.headers['Authorization'] = `Bearer ${refreshToken}`;
                } else {
                    throw new axios.Cancel('Logging user out');
                }
            } else {
                let accessToken = TokenService.getAccessToken();

                if (!accessToken) {
                    if (TokenService.getRefreshToken()) {
                        const response = await instance.post('/refresh');
                        TokenService.setPair(response.data);
                        accessToken = TokenService.getAccessToken();
                    } else {
                        // TODO Dispatch Logout
                        throw new axios.Cancel('Logging user out');
                    }
                }

                config.headers['Authorization'] = `Bearer ${accessToken}`;
            }
        }

        return config;
    },
    (error) => {
        return Promise.reject(error);
    }
);

export default instance;