import { AxiosRequestConfig, AxiosResponse } from "axios";

import client from "@common/api";
import { RouteUndefinedException } from "@common/exceptions";

// Subject to change
const API_URL: string | undefined = process.env.REACT_APP_CARTOGRAPHER_API_URL || 'https://8t477r8ejh.execute-api.us-east-1.amazonaws.com/dev/map/';

export default async function cartographer(method: "GET" | "POST", route: string | undefined, config: AxiosRequestConfig = {}): Promise<AxiosResponse> {
    if(!route) {
        throw RouteUndefinedException;
    }

    return await client(method, API_URL + route, config);
}
