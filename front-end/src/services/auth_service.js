import axios from 'axios'

const baseURL = 'http://localhost:5000/api/v1/'

const AxiosInstance = axios.create({
    baseURL
});

AxiosInstance.interceptors.response.user(
    (response) => response,
    (error) => {
        return Promise.reject(error)
    }
)

export default AxiosInstance