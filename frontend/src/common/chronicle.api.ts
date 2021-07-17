import { AxiosRequestConfig, AxiosResponse } from "axios";

import client from "@common/api";

// Subject to change
const API_URL: string = 'https://pc71cber55.execute-api.us-east-1.amazonaws.com/dev/';

export default async function chronicle(method: 'GET' | 'POST', route: string, config: AxiosRequestConfig = {}): Promise<AxiosResponse> {
    return await client(method, API_URL + route, config);
}
