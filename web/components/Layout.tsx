import Head from 'next/head'
import { useRouter } from 'next/router'
import { useContext } from 'react'

import AppBar from '@mui/material/AppBar'
import Box from '@mui/material/Box'
import Button from '@mui/material/Button'
import Card from '@mui/material/Card'
import Divider from '@mui/material/Divider'
import Drawer from '@mui/material/Drawer'
import ListItem from '@mui/material/ListItem'
import ListItemText from '@mui/material/ListItemText'
import Toolbar from '@mui/material/Toolbar'
import Typography from '@mui/material/Typography'

import { UserContext } from '../pages/_app'

import styles from '../styles/Layout.module.css'

export type LayoutPropsType = {
  children: React.ReactNode
  title: string
  hideMenu?: boolean
}

const drawerWidth = 240

export default function Layout(props: LayoutPropsType) {
  const { userInfo } = useContext(UserContext) // ユーザcontextを利用
  const router = useRouter()

  // ログアウト処理
  const handleLogout = () => {
    sessionStorage.removeItem('access_token')
    router.push('/login')
  }

  return (
    <div>
      <Head>
        <title>{`${props.title} | FastAPI practice`}</title>
        <meta name="description" content={props.title} />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main>
        {props.hideMenu ? (
          <div className={styles.noHeader}>{props.children}</div>
        ) : (
          <Box className={styles.withHeader} sx={{ display: 'flex' }}>
            <AppBar position="fixed" sx={{ zIndex: (theme) => theme.zIndex.drawer + 1 }}>
              <Toolbar>
                <Typography variant="h6" sx={{ ml: 2, flexGrow: 1 }}>
                  FastAPI practice
                </Typography>
                <Typography sx={{ mr: 4 }}>ログイン中 : {userInfo?.name}</Typography>
                <Button color="inherit" onClick={handleLogout}>
                  ログアウト
                </Button>
              </Toolbar>
            </AppBar>
            <Drawer
              anchor="left"
              variant="permanent"
              sx={{
                width: drawerWidth,
                [`& .MuiDrawer-paper`]: { width: drawerWidth, boxSizing: 'border-box' },
              }}
            >
              <Toolbar />
              <Box sx={{ overflow: 'auto' }}>
                {[
                  { uri: '/', text: 'ホーム' },
                  { uri: '/settings', text: '設定' },
                ].map((sidebarInfo, index) => (
                  <div key={index}>
                    <ListItem
                      button
                      sx={{
                        height: 60,
                        backgroundColor: router.pathname === sidebarInfo.uri ? '#BCD7EE' : 'white',
                        '&:hover': { backgroundColor: '#BCD7EE' },
                      }}
                      onClick={() => router.push(sidebarInfo.uri)}
                    >
                      <ListItemText primary={sidebarInfo.text} />
                    </ListItem>
                    <Divider />
                  </div>
                ))}
              </Box>
            </Drawer>
            <Card
              sx={{
                margin: '14px',
                width: '100%',
                padding: '20px 30px',
              }}
            >
              {props.children}
            </Card>
          </Box>
        )}
      </main>
    </div>
  )
}
