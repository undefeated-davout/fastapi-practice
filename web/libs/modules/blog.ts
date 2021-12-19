import { UseSWRAPI } from './api'

export const SWR_GET_BLOGS = '/blogs/'

export function GetBlogs() {
  return UseSWRAPI(SWR_GET_BLOGS)
}
