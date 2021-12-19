import { render, screen } from '@testing-library/react'
import '@testing-library/jest-dom/extend-expect'
import { useState } from 'react'

import AlertDialog, { AlertDialogPropsType } from './AlertDialog'

describe('AlertDialogテスト', () => {
  let dummyProps: AlertDialogPropsType
  beforeEach(() => {
    dummyProps = {
      open: true,
      title: 'サンプルタイトル',
      content: 'サンプル本文',
      doYes: () => console.log('Yesボタンの動作'),
    }
  })

  it('OKボタンのみ（キャンセルボタンなし）', () => {
    dummyProps.noButtonFlag = false
    render(<AlertDialog {...dummyProps} />)
    expect(screen.getByText(dummyProps.title)).toBeInTheDocument()
    expect(screen.getByText(dummyProps.content)).toBeInTheDocument()
    expect(screen.getByText('OK')).toBeInTheDocument()
    expect(screen.queryByText('キャンセル')).not.toBeInTheDocument()
  })
  it('OKボタン&キャンセルボタン', () => {
    dummyProps.noButtonFlag = true
    dummyProps.doNo = () => console.log('キャンセルボタンの動作')
    render(<AlertDialog {...dummyProps} />)
    expect(screen.getByText(dummyProps.title)).toBeInTheDocument()
    expect(screen.getByText(dummyProps.content)).toBeInTheDocument()
    expect(screen.getByText('OK')).toBeInTheDocument()
    expect(screen.queryByText('キャンセル')).toBeInTheDocument()
  })
})
