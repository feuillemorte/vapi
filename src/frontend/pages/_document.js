import { Html, Head, Main, NextScript } from "next/document";
import Container from 'react-bootstrap/Container';

const Document = () => {
    return (
        <Html>
            <Head>
                <link rel="preconnect" href="https://fonts.googleapis.com" />
                <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="true" />
                <link href="https://fonts.googleapis.com/css2?family=Rubik:wght@300;400;500;600;700&display=swap" rel="stylesheet" />
                <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.2.3/css/bootstrap.min.css" integrity="sha512-SbiR/eusphKoMVVXysTKG/7VseWii+Y3FdHrt0EpKgpToZeemhqHeZeLWLhJutz/2ut2Vw1uQEj2MbRF+TVBUA==" crossOrigin="anonymous" referrerPolicy="no-referrer" />
            </Head>
            <body>
                <Container fluid={true}>
                    <Main />
                </Container>
                <NextScript />
            </body>
        </Html>
    );
};

export default Document;
