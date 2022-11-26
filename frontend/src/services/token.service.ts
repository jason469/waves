const REFRESH_TOKEN_KEY = 'refreshToken';
const ACCESS_TOKEN_KEY = 'accessToken'

interface TokenPair {
    access : string,
    refresh: string
}

class TokenService {
    private static isTokenExpired(token: string){
        const [_, payload, __] = token.split(".");
        return JSON.parse(payload).exp * 1000 > Date.now()
    }

    static getRefreshToken(): string | null {
        const token = localStorage.getItem(REFRESH_TOKEN_KEY);
        if(token){
            return !TokenService.isTokenExpired(token) ? token : null;
        }else{
            return null
        }
    }

    static setRefreshToken(token: string) {
        localStorage.setItem(REFRESH_TOKEN_KEY, token) ;
    }

    static deleteRefreshToken () {
        localStorage.removeItem(REFRESH_TOKEN_KEY);
    }

    static getAccessToken(): string | null {
        const token = localStorage.getItem(ACCESS_TOKEN_KEY);
        if(token){
            return !TokenService.isTokenExpired(token) ? token : null;
        }else{
            return null
        }
    }

    static setAccessToken(token: string) {
        localStorage.setItem(ACCESS_TOKEN_KEY, token);
    }

    static deleteAccessToken() {
        localStorage.removeItem(ACCESS_TOKEN_KEY);
    }

    static getPair(): TokenPair {
        return {
            access: TokenService.getAccessToken() || "",
            refresh: TokenService.getRefreshToken() || ""
        };
    }

    static setPair(pair: TokenPair) {
        TokenService.setAccessToken(pair.access);
        TokenService.setRefreshToken(pair.refresh);
    }

    static deletePair() {
        TokenService.deleteAccessToken();
        TokenService.deleteRefreshToken();
    }
}

export default TokenService;