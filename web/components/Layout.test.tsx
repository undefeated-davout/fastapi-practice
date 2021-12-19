import { render, screen, waitFor } from '@testing-library/react'
import '@testing-library/jest-dom/extend-expect'

import Layout, { LayoutPropsType } from './Layout'

// モック画面遷移
jest.mock('next/router', () => ({
  useRouter() {
    return {
      asPath: '/',
    }
  },
}))

describe('Layoutテスト', () => {
  let dummyProps: LayoutPropsType
  beforeEach(() => {
    dummyProps = {
      children: <div>テストコンテンツ</div>,
      title: 'テストタイトル',
      hideMenu: false,
    }
  })

  it('ホーム表示時確認', async () => {
    render(<Layout {...dummyProps} />)
    // タイトル（テストでエミュレートできていないようなので後回し）
    // コンテンツ
    expect(screen.getByText('テストコンテンツ')).toBeInTheDocument()
    // サイドバー
    expect(screen.getByText('ホーム')).toBeInTheDocument()
    expect(screen.getByText('設定')).toBeInTheDocument()
  })
})
