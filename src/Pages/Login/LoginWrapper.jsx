import styled from 'styled-components'

const LoginWrapper = styled.div`
   display: flex;
   flex-direction: column;
   justify-content: center;
   align-items: center;

   h1{
      color: #00DCA1;
      font-weight: 500;
      font-size: 7rem;
      transform: translateY(-30px);
   } 

   @media only screen and (max-width: 600px){
      h1{
         font-size: 4.5rem;
      }
   }
`

export default LoginWrapper;