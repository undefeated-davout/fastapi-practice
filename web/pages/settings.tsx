import type { NextPage } from 'next'

import Typography from '@mui/material/Typography'

import Layout from '../components/Layout'

const Home: NextPage = () => {
  return (
    <Layout title="設定">
      <Typography variant="h6" sx={{ float: 'left' }}>
        設定
      </Typography>
    </Layout>
  )
}

export default Home
