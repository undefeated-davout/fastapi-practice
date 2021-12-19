import { useEffect, useState } from 'react'

import Button from '@mui/material/Button'
import Dialog from '@mui/material/Dialog'
import DialogTitle from '@mui/material/DialogTitle'
import DialogContent from '@mui/material/DialogContent'
import DialogActions from '@mui/material/DialogActions'
import DialogContentText from '@mui/material/DialogContentText'

export type AlertDialogPropsType = {
  open: boolean
  title: string
  content: string
  noButtonFlag?: boolean
  doYes: any
  doNo?: any
}

const AlertDialog = (props: AlertDialogPropsType) => {
  const [open, setOpen] = useState(props.open)

  useEffect(() => {
    setOpen(props.open)
  }, [props.open])

  const handleYesButton = () => {
    setOpen(false)
    props.doYes()
  }

  const handleNoButton = () => {
    setOpen(false)
    if (props.doNo) {
      props.doNo()
    }
  }

  return (
    <Dialog
      open={open}
      aria-labelledby="alert-dialog-title"
      aria-describedby="alert-dialog-description"
      fullWidth
      maxWidth="xs"
    >
      <DialogTitle id="alert-dialog-title">{props.title}</DialogTitle>
      <DialogContent>
        <DialogContentText id="alert-dialog-description" style={{ whiteSpace: 'pre-line' }}>
          {props.content}
        </DialogContentText>
      </DialogContent>
      <DialogActions>
        {props.noButtonFlag && (
          <Button onClick={handleNoButton} color="primary">
            キャンセル
          </Button>
        )}
        <Button onClick={handleYesButton} color="primary">
          OK
        </Button>
      </DialogActions>
    </Dialog>
  )
}

export default AlertDialog
