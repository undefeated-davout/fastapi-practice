import type { NextPage } from 'next'

import Typography from '@mui/material/Typography'

import Layout from '../components/Layout'

const Home: NextPage = () => {
  return (
    <Layout title="ホーム">
      <Typography variant="h6" sx={{ float: 'left' }}>
        ホーム
      </Typography>
    </Layout>
  )
}

export default Home
