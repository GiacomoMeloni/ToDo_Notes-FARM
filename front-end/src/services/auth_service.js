import axios from 'axios'

const baseURL = 'http://localhost:5000/api/todo/v1/'

const AxiosInstance = axios.create({
    baseURL
});

AxiosInstance.interceptors.response.use(
    (response) => response,
    (error) => {
        return Promise.reject(error)
    }
)

export default AxiosInstance