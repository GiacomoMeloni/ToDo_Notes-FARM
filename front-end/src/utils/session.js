import AxiosInstance from "../services/auth_service";

export const setSession = (accessToken, refreshToken = null) => {
    if (accessToken){
        localStorage.setItem("accessToken", accessToken);
        AxiosInstance.defaults.headers.common["Authorization"] = `Bearer ${accessToken}`;
    }else {
        localStorage.removeItem("accessToken");
        delete AxiosInstance.defaults.headers.common["Authorization"];
    }

    if (refreshToken){
        localStorage.setItem("refreshToken", refreshToken);
    }
}

export const resetSession = () => {
    localStorage.removeItem("accessToken");
    localStorage.removeItem("refreshToken");
    delete AxiosInstance.defaults.headers.common["Authorization"];
}