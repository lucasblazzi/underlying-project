import React, { Component } from "react";
import MetaTags from "react-meta-tags";
import { Row, Col, Card, CardBody, CardTitle, Container, Media, TabPane } from "reactstrap"

class newPage extends Component {
  render() {
    return (
      <React.Fragment>
        <div className="page-content">
          <MetaTags>
            <title>Nova página</title>
          </MetaTags>
          <Container fluid>
            <h4>Título da página (opcional)</h4>
            <Row>
              <Col>
                <Card>
                  <CardBody>
                    <div>
                      <CardTitle className="mb-5">
                        Título do card
                      </CardTitle>
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

export default newPage;