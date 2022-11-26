import api from "./api";
import TokenService from "./token.service";

const AuthService = {
    login: (username: string, password: string) => {
        return api
            .post('/login', {
                username,
                password
            })
            .then(response => {
                TokenService.setPair(response.data);
                return response.data;
            });

    },
    logout: async () => {
        const refreshToken = TokenService.getRefreshToken();
        if(refreshToken){
            await api.post('/logout');
        }
        TokenService.deletePair();
    }
};

export default AuthService;