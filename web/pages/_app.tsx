import type { AppProps } from 'next/app'
import { useState, useEffect, createContext } from 'react'

import { GetCurrentUser } from '../libs/modules/auth'
import { UserType } from '../libs/types/user'

import '../styles/globals.css'

// アプリ全体でアクセスできる情報を定義する
export const UserContext = createContext<{
  userInfo: UserType | null
  setUserInfo: React.Dispatch<React.SetStateAction<UserType | null>>
}>({
  userInfo: null,
  setUserInfo: () => {},
})

function UtilApp({ Component, pageProps, router }: AppProps) {
  const [userInfo, setUserInfo] = useState<UserType | null>(null)
  const [displayReadyFlag, setDisplayReadyFlag] = useState(false)

  useEffect(() => {
    ;(async function () {
      let isLoggedIn = false
      const currentUser = await GetCurrentUser()
      if (!currentUser?.detail) {
        // ユーザ情報取得
        setUserInfo({ name: currentUser.name })
        isLoggedIn = true
      } else {
        setUserInfo(null)
      }
      if (isLoggedIn && ['/login', '/_error'].indexOf(router.pathname) > -1) {
        // ログイン状態でloginページor不正なページにアクセスしたらトップページへリダイレクト
        router.push('/')
        return
      } else if (!isLoggedIn && router.pathname !== '/login') {
        // ログアウト状態でloginページ以外にアクセスしたらloginページへリダイレクト
        router.push('/login')
        return
      }
      setDisplayReadyFlag(true) // ログイン判定が完了したら描画準備完了
    })()
  }, [router, router.pathname])

  // 表示準備完了するまで何も表示しない
  if (!displayReadyFlag) {
    return <></>
  }

  return (
    <UserContext.Provider value={{ userInfo, setUserInfo }}>
      <Component {...pageProps} />
    </UserContext.Provider>
  )
}

export default UtilApp
