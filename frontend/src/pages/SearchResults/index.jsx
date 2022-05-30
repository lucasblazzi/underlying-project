import React, { Component } from "react";
import MetaTags from "react-meta-tags";
import { Row, Col, Card, CardBody, CardTitle, Container, NavItem, Table, Button, } from "reactstrap";
import { withRouter, Link } from "react-router-dom";
import PropTypes from "prop-types";

class SearchResults extends Component {
  constructor(props) {
    super(props);
    this.state = {
      busca: null,
      result: null,
    };
  }

  componentDidMount() {
    const self = this;
    var termo;
    if (self.props.location.state.busca != null) {
      termo = self.props.location.state.busca;
      self.setState({ busca: self.props.location.state.busca });
    }
    console.log("Busca:", termo);
    var raw = JSON.stringify({
      "query": termo
    });

    var requestOptions = {
      method: 'POST',
      body: raw,
      redirect: 'follow'
    };

    fetch("https://lgbxzn9a97.execute-api.us-east-1.amazonaws.com/v1/search", requestOptions)
      .then(response => response.json())
      .then(result => {
        console.log(result);
        self.setState({ result: result });
      })
      .catch(error => console.log('error', error));
  }

  render() {
    let tableRender;
    if (this.state.result != null) {
      if (this.state.result.length != 0) {
        var body;
        tableRender = <div className="table-responsive">
          <Table className="table align-middle table-nowrap">
            <tbody>
              {this.state.result.map((element, index) => (
                <tr key={index}>
                  <td>
                    <div>
                      <h5 className="font-size-14 mb-1">{element.name} | {element.name_underlying}</h5>
                      <p className="text-muted mb-0">Data: {element.date} | Validade: {element.expiration_date}</p>
                    </div>
                  </td>

                  <td>
                    <div className="text-end">
                      <h5 className="font-size-14 mb-0">{element.type}</h5>
                    </div>
                  </td>

                  <td>
                    <div className="text-end">
                      <h5 className="font-size-14 text-muted mb-0">
                        Preço de fechamento: {element.close_price} | Preço de exercício: {element.exercise_price}
                      </h5>
                    </div>
                  </td>

                  <td >
                    <div className="text-end">
                      <h5 className="font-size-20 mb-0">
                        <Link to={{pathname: "../opts", state: {name: element.name, id: element.id}}} style={{ "border": "none" }}>
                          <i className='bx bx-right-arrow-circle'></i>
                        </Link>
                      </h5>
                    </div>
                  </td>
                </tr>
              ))}
            </tbody>
          </Table>
        </div>
      }
      else tableRender = (
        <Row>
          <div style={{ "text-align": "center" }}>
            <h1>Não há resultados para esta busca!</h1>
            <Link to={{pathname: "../search",}}>
              <Button
                color="primary"
                className="btn btn-primary "
              >Voltar</Button>
            </Link>
          </div>
        </Row>
      );
    }
    return (
      <React.Fragment>
        <div className="page-content">
          <MetaTags>
            <title>Resultados</title>
          </MetaTags>
          <Container fluid>
            <h4>Resultados</h4>
            <Row>
              <Col>
                <Card>
                  <CardBody>
                    <div>
                    </div>
                    {tableRender}
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

SearchResults.propTypes = {
  location: PropTypes.object,
}

export default withRouter(SearchResults);