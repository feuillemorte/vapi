import { useCallback, useEffect, useState } from "react";


const useGetRequest = (url) => {
    const get = useCallback(async () => {
        const response = await fetch(url);
        const result = await response.json();
        return result;
    }, [url]);
    return get;
};

export default useGetRequest;
