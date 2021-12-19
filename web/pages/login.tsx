import type { NextPage } from 'next'
import { useRouter } from 'next/router'
import { useState } from 'react'

import Box from '@mui/material/Box'
import Button from '@mui/material/Button'
import Card from '@mui/material/Card'
import CardContent from '@mui/material/CardContent'
import TextField from '@mui/material/TextField'
import Typography from '@mui/material/Typography'

import AlertDialog from '../components/AlertDialog'
import Layout from '../components/Layout'
import { PostLogin } from '../libs/modules/auth'

const Login: NextPage = () => {
  const [isActiveDialog, setIsActiveDialog] = useState(false)
  const router = useRouter()

  // ログイン処理
  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault()
    const data = new FormData(event.currentTarget)
    PostLogin(String(data.get('user_id')), String(data.get('password'))).then((res) => {
      if (!res?.detail) {
        sessionStorage.setItem('access_token', res.access_token)
        router.push('/')
      } else {
        setIsActiveDialog(true)
      }
    })
  }

  return (
    <Layout title="ログイン" hideMenu={true}>
      <Card sx={{ maxWidth: 640, maxHeight: 480, margin: 'auto', padding: '60px 100px' }}>
        <CardContent>
          <Typography variant="h6" align="center">
            FastAPI practice
          </Typography>
          <Box component="form" onSubmit={handleSubmit} noValidate sx={{ mt: 5 }}>
            <TextField
              margin="normal"
              required
              fullWidth
              id="user_id"
              label="ユーザID"
              name="user_id"
            />
            <TextField
              margin="normal"
              required
              fullWidth
              name="password"
              label="パスワード"
              type="password"
              id="password"
              autoComplete="on"
            />
            <Button type="submit" fullWidth variant="contained" sx={{ mt: 6, mb: 2 }}>
              ログイン
            </Button>
          </Box>
        </CardContent>
      </Card>
      <AlertDialog
        open={isActiveDialog}
        title="ログインエラー"
        content={'メールアドレスまたはパスワードが違います'}
        doYes={() => setIsActiveDialog(false)}
      />
    </Layout>
  )
}

export default Login
