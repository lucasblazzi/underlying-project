import React, { Component } from "react";
import MetaTags from "react-meta-tags";
import { Row, Col, Card, CardBody, CardTitle, Container, Media, TabPane } from "reactstrap"

class duvidas extends Component {
    render() {
        return (
            <React.Fragment>
                <div className="page-content">
                    <MetaTags>
                        <title>Nova página</title>
                    </MetaTags>
                    <Container fluid>
                        <h4>Questões</h4>
                        <Row>
                            <Col>
                                <Card>
                                    <CardBody>
                                        <div>
                                            <Media className="faq-box mb-4">
                                                <div className="faq-icon me-3">
                                                    <i className="bx bx-help-circle font-size-20 text-success" />
                                                </div>
                                                <Media body>
                                                    <h5 className="font-size-15">
                                                        Como fazer requisições?
                                                    </h5>
                                                    <p className="text-muted">
                                                        As requisições &#123; get &#125; são feitas através do API_helper (helpers/api_hepler.js).<br />
                                                        Os demais tipos de requisições estão usando o fetch, porque esse API_helper é uma merda.
                                                    </p>
                                                </Media>
                                            </Media>
                                            <Media className="faq-box mb-4">
                                                <div className="faq-icon me-3">
                                                    <i className="bx bx-help-circle font-size-20 text-success" />
                                                </div>
                                                <Media body>
                                                    <h5 className="font-size-15">
                                                        Como criar nova página?
                                                    </h5>
                                                    <p className="text-muted">
                                                        As novas páginas podem ser criadas copiando o conteúdo da página <b>newPage.jsx &#40;src/pages/newPage.jsx&#41;</b><br />
                                                        Se uma página for montada usando mais de um arquivo, é recomendado que crie uma pasta para aquela página.<br />
                                                        Depois de criada a página, ela tem que ser adicionada ao arquivo de rotas, presente em <b>src/routes/index.js</b>, no array de rotas protegidas &#40;authProtectedRoutes&#41;:<br />
                                                        <code>
                                                            const authProtectedRoutes = &#91; <br />
                                                            &#123; path: &quot;/new-page&quot;, component: newPage &#125; <br />
                                                            &#93;
                                                        </code>
                                                    </p>
                                                </Media>
                                            </Media>
                                            <Media className="faq-box mb-4">
                                                <div className="faq-icon me-3">
                                                    <i className="bx bx-help-circle font-size-20 text-success" />
                                                </div>
                                                <Media body>
                                                    <h5 className="font-size-15">
                                                        Analisando os dados recebidos.
                                                    </h5>
                                                    <p className="text-muted">
                                                        Breve documentação de como trabalhar com os dados recebidos na requisição:
                                                        <a href="https://docs.google.com/document/d/1weVGcTL2X7X-pV6LRkc1I92bPaCHaUbBfJUTdCjuEMc/edit?usp=sharing" target="_blank" rel="noopener noreferrer"> Link</a>
                                                    </p>
                                                </Media>
                                            </Media>
                                        </div>
                                    </CardBody>
                                </Card>
                            </Col>
                        </Row>
                    </Container>
                </div>
            </React.Fragment>
        );
    }
}

export default duvidas;