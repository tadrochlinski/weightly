import React from 'react'
import PageWrapper from '../../Components/PageWrapper'
import LoginWrapper from './LoginWrapper'
import GoogleButton from 'react-google-button'

export default function Login() {
  return (
    <PageWrapper>
      <LoginWrapper>
        <h1>Weightly</h1>
        <GoogleButton label='Log in with Google' type='light'/>
      </LoginWrapper>
    </PageWrapper>
  )
}
