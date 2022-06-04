import React, { Component } from "react";
import MetaTags from "react-meta-tags";
import { Row, Col, Card, CardBody, CardImg, Container, Input, Button, Table, Spinner, InputGroup, InputGroupAddon } from "reactstrap";
import logo from "../../assets/images/logo-underlying.png";
import { Link, useHistory } from "react-router-dom";
import "./dots.css";
import InfiniteScroll from "react-infinite-scroll-component";
import PropTypes from "prop-types";

// const history = useHistory();

class Search extends Component {
  constructor(props) {
    super(props);
    this.state = {
      busca: "",
      loading: false,
      result: [],
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
    console.log("Busca value = ", value);
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
                            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam quis massa dolor. Quisque at turpis at elit sagittis suscipit. Quisque non neque eget mauris ornare semper.</p>
                            <Button color="info" onClick={() => {window.location.href = "../coming-soon"}}>Acessar</Button>
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
                            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam quis massa dolor. Quisque at turpis at elit sagittis suscipit. Quisque non neque eget mauris ornare semper.</p>
                            <Button color="info" onClick={() => {window.location.href = "../coming-soon"}}>Acessar</Button>
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
                            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam quis massa dolor. Quisque at turpis at elit sagittis suscipit. Quisque non neque eget mauris ornare semper.</p>
                            <Button color="info" onClick={() => {window.location.href = "../coming-soon"}}>Acessar</Button>
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
              <Col style={{ "textAlign": "center", "marginTop": "15px"}}>
                <Row style={{ "justifyContent": "center" }}>
                  <Col xl={{ "size": "8" }}>
                    <Input
                      type="text"
                      id="busca"
                      required
                      onChange={(e) => this.onChangeHandler(e)}
                      placeholder="Buscar..."
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
                  <InfiniteScroll
                    dataLength={this.state.result.length}
                    next={this.renderOptions}
                    hasMore={true}
                  >
                    <div className="table-responsive">
                      <Table className="table align-middle table-nowrap">
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
                          ))}
                        </tbody>
                      </Table>
                    </div>
                  </InfiniteScroll>
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