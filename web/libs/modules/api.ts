import useSWR from 'swr'

export const fetcher = async (
  endpoint: string,
  method: string = 'GET',
  body: any,
): Promise<any> => {
  // トークンをブラウザで保持しているならヘッダにセット
  const accessToken = sessionStorage.getItem('access_token')
  const headers = accessToken
    ? {
        Authorization: 'Bearer ' + accessToken,
      }
    : undefined
  return fetch(`${process.env.NEXT_PUBLIC_API_URL}${endpoint}`, {
    method: method,
    body: body,
    headers: headers,
  }).then((res) => res.json())
}

export function UseSWRAPI(endpoint: string) {
  const { data, error } = useSWR(endpoint, fetcher)
  return {
    data: data || null,
    isLoading: !error && !data,
    isError: !!error,
  }
}
