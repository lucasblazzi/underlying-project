import React, { Component } from "react";
import MetaTags from "react-meta-tags";
import { Row, Col, Card, CardBody, CardImg, Container, Input, Button, Table, Spinner, InputGroup, InputGroupAddon } from "reactstrap";
import "./dots.css";
import InfiniteScroll from "react-infinite-scroll-component";
import PropTypes from "prop-types";
import { Link } from "react-router-dom"

// const history = useHistory();

class Search extends Component {
  constructor(props) {
    super(props);
    this.state = {
      busca: "",
      loading: false,
      result: null,
      count: 0,
    }
    this.timeout = 0;
    this.renderOptions = this.renderOptions.bind(this);
  }

  search(requestOptions) {
    this.setState({ loading: true })
    fetch("https://lgbxzn9a97.execute-api.us-east-1.amazonaws.com/v1/search", requestOptions)
      .then(response => response.json())
      .then(result => {
        console.log(result);
        this.setState({ result: this.state.result.concat(result), loading: false });
      })
      .catch(error => console.log('error', error));
  }

  onChangeHandler(e) {
    this.setState({ result: [], });
    this.setState({ count: 0 });
    var requestOptions = {
      method: 'POST',
      body: JSON.stringify({
        "query": e.target.value,
        "from": 0,
        "size": 10
      }),
      redirect: 'follow'
    };
    if (this.timeout) clearTimeout(this.timeout);

    document.getElementById("load").hidden = false;

    this.timeout = setTimeout(() => {
      this.search(requestOptions);
      this.setState({ busca: e.target.value });
      document.getElementById("load").hidden = true;
    }, 700);
  };

  renderOptions() {
    var self = this;
    var next = self.state.count + 10;
    var value = document.getElementById("busca").value;
    //console.log("Busca value = ", value);
    var requestOptions = {
      method: 'POST',
      body: JSON.stringify({
        "query": value,
        "from": next,
        "size": 10
      }),
      redirect: 'follow'
    };

    if (self.timeout) clearTimeout(self.timeout);
    self.timeout = setTimeout(() => {
      self.search(requestOptions);
      self.setState({ busca: value, count: next });
    }, 700);
  }

  render() {
    var resultContent;
    if (this.state.result == null) {
      resultContent = <div></div>;
    } else {
      resultContent = <InfiniteScroll
        dataLength={this.state.result.length}
        next={this.renderOptions}
        hasMore={true}
      >
        <div className="table-responsive">
          <Table className="table align-middle table-nowrap custom-hover">
            <tbody>
              {this.state.result.map((element, index) => (
                <tr
                  key={index}
                  style={{ "cursor": "pointer" }}
                  onClick={this.routingFunction = () => {
                    this.props.history.push({
                      pathname: '../opts',
                      state: { name: element.name, id: element.id },
                    });
                  }}
                >
                  <td>
                    <div>
                      <h5 className="font-size-14 mb-1">{element.name} | {element.name_underlying} | {element.type}</h5>
                      <p className="text-muted mb-0">Data: {element.date} |
                        Vencimento: {element.expiration_date}</p>
                    </div>
                  </td>

                  <td>
                    <div className="text-end">
                      <h5 className="font-size-14 text-muted mb-0">
                        Preço de fechamento: {element.close_price}<br />
                        Preço de exercício: {element.exercise_price}
                      </h5>
                    </div>
                  </td>
                </tr>
              ))
              }
            </tbody>
          </Table>
        </div>
      </InfiniteScroll>
    }
    return (
      <React.Fragment>
        <div className="page-content">
          <MetaTags>
            <title>Pesquisa</title>
          </MetaTags>
          <Container fluid>
            {/* 3 Cards */}
            <Row>
              <Col>
                <Card>
                  <CardBody>
                    <Row style={{ "textAlign": "center" }}>
                      <Col xl="4">
                        <Card>
                          <CardBody>
                            <i className="bx bx-chart me-2 font-size-24"></i>
                            <br />
                            <h4>Estratégias</h4>
                            <hr />
                            <p>Monte suas próprias estratégias com base em opções reais do mercado e simule operações com opções fictícas criadas em tempo real</p>
                            <Link
                              className="nav-link dropdown-toggle arrow-none"
                              to="/strategies"
                            >
                              <Button color="info" onClick={() => { null }}>Acessar</Button>
                            </Link>
                          </CardBody>
                        </Card>
                      </Col>
                      <Col xl="4">
                        <Card>
                          <CardBody>
                            <i className="bx bx-grid-alt me-2 font-size-24"></i>
                            <br />
                            <h4>Grade de opções</h4>
                            <hr />
                            <p>Encontre a grade de opções de ativos com base em seu ativo base. Aqui você pode encontrar todas as opções de uma ação utilizando seu ticker</p>
                            <Link
                              className="nav-link dropdown-toggle arrow-none"
                              to="/coming-soon"
                            >
                              <Button color="info" onClick={() => { null }}>Acessar</Button>
                            </Link>
                          </CardBody>
                        </Card>
                      </Col>
                      <Col xl="4">
                        <Card>
                          <CardBody>
                            <i className="bx bx-book-bookmark me-2 font-size-24"></i>
                            <br />
                            <h4>Glossário</h4>
                            <hr />
                            <p>Tire suas dúvidas em relação a termos comuns e conceitos relacionados ao mercado de opções</p>
                            <Link
                              className="nav-link dropdown-toggle arrow-none"
                              to="/glossary"
                            >
                              <Button color="info" onClick={() => { null }}>Acessar</Button>
                            </Link>
                          </CardBody>
                        </Card>
                      </Col>
                    </Row>
                  </CardBody>
                </Card>
              </Col>

            </Row>
            {/* FIM 3 Cards */}
            <Row >
              <Col style={{ "textAlign": "center", "marginTop": "20px" }}>
                <Row style={{ "justifyContent": "center" }}>
                  <div style={{ "textAlign": "center", "marginBottom": "20px", "marginTop": "30px" }}><h4>Buscar Opções:</h4></div>
                  <Col xl={{ "size": "8" }}>
                    <Input
                      type="text"
                      id="busca"
                      required
                      onChange={(e) => this.onChangeHandler(e)}
                      placeholder="Buscar..."
                      style={{ "marginBottom": "2rem" }}
                    >
                      <i className="bx bx-search me-2"></i>
                    </Input>
                  </Col>
                </Row>
              </Col>

              {/* Loading de pesquisa */}
              <Row id="load" hidden>
                <Col xl={{ size: 8, offset: 6 }} md={{ size: 8, offset: 6 }} sm="12" ><div className="dot-flashing mt-2"></div></Col>
              </Row>
              {/* FIM Loading de pesquisa */}

              {/* Resultado da pesquisa */}
              <Row style={{ "justifyContent": "center" }}>
                <Col xl={{ "size": "8" }} >
                  {resultContent}

                </Col>
              </Row>
              {/* FIM Resultado da pesquisa */}
            </Row>
          </Container>
        </div>
      </React.Fragment>
    );
  }
}

Search.propTypes = {
  history: PropTypes.any,
}

export default Search;