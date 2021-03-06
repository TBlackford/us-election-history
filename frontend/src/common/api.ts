import axios, { AxiosRequestConfig, AxiosResponse } from 'axios';
import { ImplementationException } from "@common/exceptions";

//TODO: this API
const API_URL: string = '';


const get = (route: string, config: AxiosRequestConfig) => {
    return axios.get(route, config);
}

const post = (route: string, config: AxiosRequestConfig) => {
    return axios.post(API_URL + route, config);
}

export default async function client(method: 'GET' | 'POST', route: string, config: AxiosRequestConfig = {}): Promise<AxiosResponse> {
    config = Object.assign(config, {
        // Add in any necessary headers
    });

    switch (method) {
        case 'GET':
            return await get(API_URL + route, config);
        case 'POST':
            return await post(API_URL + route, config);

        default:
            throw ImplementationException;
    }
}
