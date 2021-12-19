import { fetcher } from './api'

export async function PostLogin(username: string, password: string): Promise<any> {
  const formData = new FormData()
  formData.append('username', username)
  formData.append('password', password)
  return fetcher('/login', 'POST', formData)
}

export async function GetCurrentUser(): Promise<any> {
  return fetcher('/users/me', 'GET', null)
}
