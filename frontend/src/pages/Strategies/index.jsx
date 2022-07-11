import React, { Component } from "react";
import MetaTags from "react-meta-tags";
import { Row, Col, Card, CardBody, Container, Input, Spinner, Button, Collapse, Modal } from "reactstrap"
import { Table, Thead, Tbody, Tr, Td, Th } from "react-super-responsive-table";
import OptsShortChart from "pages/Opts/OptsShortChart";
import Payoff from "./payoff";
import SearchBar from "./SearchBar";
import toastr from "toastr"
import "toastr/build/toastr.min.css"

class Strategies extends Component {
  constructor(props) {
    super(props);
    this.state = {
      strategyData: null,
      modal_create_opt: false,
      options: [],
      chartModal: [false],
      isCreated: false,
      createResponse: null,
    }
    this.req = this.req.bind(this);
    this.removeBodyCss = this.removeBodyCss.bind(this);
    this.modal_create_opt = this.modal_create_opt.bind(this);
    this.handleInputChange = this.handleInputChange.bind(this);
    this.addOpt = this.addOpt.bind(this);
    this.modal_chart = this.modal_chart.bind(this);
    this.changeTransactionType = this.changeTransactionType.bind(this);
    this.changeStrategy = this.changeStrategy.bind(this);
    this.updateStrategy = this.updateStrategy.bind(this);
  }

  addOpt(value) {
    //console.log("Valor recebido:", value);
    this.setState({ options: this.state.options.concat(value) }, () => {
      this.changeStrategy();
    });
  }

  changeStrategy() {
    var bodyRaw = JSON.stringify({ "strategy": this.state.options })
    //console.log("Body Raw: ", bodyRaw);
    this.req("https://jdmgjcpm1m.execute-api.us-east-1.amazonaws.com/v1/payoff", bodyRaw, "strategyData");
  }

  handleInputChange(event) {
    const target = event.target;
    const value = target.value;
    const name = target.name;
    //console.log(value);

    this.setState({
      [name]: value,
    });
  }


  /**
  * Recebe a url do endpoint, o corpo que passará pelo stringfy e o nome do campo que será modificado no state do construtor do Componente React
  * @param {string} url - URL da requisição
  * @param {string} requestBody - Valor a ser passado no corpo da requisição. Deve ter passado por JSON.stringify()!
  * @param {string} stateToChange - Nome do estado que será alterado
  * @param {boolean} dispatchToastr - Determina se o toastr será disparado (parâmentro opcional, padrão false)
  */
  async req(url, requestBody, stateToChange, dispatchToastr = false) {
    var requestOptions = {
      method: 'POST',
      body: requestBody,
      redirect: 'follow'
    };

    return fetch(url, requestOptions)
      .then(response => response.json())
      .then(result => {
        //console.log(`${stateToChange} = ${result}`);
        this.setState({ [stateToChange]: result });
        if (dispatchToastr) {
          toastr.success("Sucesso!");
        }
      })
      .catch(error => {
        console.log('error', error); 
        if(dispatchToastr) {
          toastr.error("Erro!");
        }
      });
  }

  //Para cada opção, fazer a requisição e guardar num array?
  // async componentDidUpdate(prevProps, prevState, snapshot) {
  //   if(prevState)
  // }

  async componentDidMount() {
    //await this.req("https://jdmgjcpm1m.execute-api.us-east-1.amazonaws.com/v1/strategy", JSON.stringify({"id":"76e2e2ae-dbdf-47e3-8539-707987c2b872"}), "strategyData");
    //console.log("Strategy Data: ", this.state.strategyData);
    //await this.req("https://jdmgjcpm1m.execute-api.us-east-1.amazonaws.com/v1/payoff", JSON.stringify({"strategy":"this.state.strategyData.strategy"}), "payoffData");
    //console.log("Payoff Data: ", this.state.payoffData);

    toastr.options = {
      timeOut: 6000,
      closeButton: true,
    };
  }

  removeBodyCss() {
    document.body.classList.add("no_padding")
  }

  modal_create_opt() {
    this.setState({
      modal_create_opt: !this.state.modal_create_opt
    });
    this.removeBodyCss()
  }

  modal_chart(i) {
    var modalIndex = this.state.chartModal;
    modalIndex[i] = !modalIndex[i];
    this.setState({
      chartModal: modalIndex
    });
    this.removeBodyCss()
  }

  changeTransactionType(value, num) {
    var newOptions = this.state.options;
    newOptions[num].transaction_type = value;
    this.setState({ options: newOptions }, () => {this.changeStrategy();});
  }

  changeContractNum(value, num) {
    if(value == "" || value == null) {
      value = 0;
    }

    var newOptions = this.state.options;
    newOptions[num].contracts = parseInt(value);
    this.setState({ options: newOptions }, () => {this.changeStrategy();});
  }

  async createStrategy(strategyName) {
    var user = localStorage.getItem("logedUser");

    var bodyRaw = JSON.stringify({
      "username": user,
      "name": strategyName,
      "strategy": this.state.options 
    })
    await this.req("https://jdmgjcpm1m.execute-api.us-east-1.amazonaws.com/v1/create", bodyRaw, "createResponse", true);
    if(this.state.createResponse != null) {
      this.setState({ isCreated: true });
    }
  }

  async updateStrategy() {
    var bodyRaw = JSON.stringify({
      "id": this.state.createResponse.id,
      "name": this.state.createResponse.name, 
      "strategy": this.state.options 
    })
    await this.req("https://jdmgjcpm1m.execute-api.us-east-1.amazonaws.com/v1/update", bodyRaw, "createResponse", true);
  }

  async shareStrategy() {
    var bodyRaw = JSON.stringify({
        "id": this.state.createResponse.id, 
        "shared": true
    })
    await this.req("https://jdmgjcpm1m.execute-api.us-east-1.amazonaws.com/v1/share", bodyRaw, "shareResponse", true);
    document.getElementById("shareBtn").style.display = "none";
  }

  render() {
    var content = null, payoff;
    if (this.state.options.length == 0) {
      content = <Tr><Td colSpan="6" style={{ "padding": "2rem" }} className="font-size-16">
          <i className='bx bx-plus-circle align-middle me-2'></i>Adicione uma opção, pelas alternativas acima!
        </Td>
      </Tr>;
      payoff = <div></div>;
    } else {
      if(this.state.strategyData == null) {
        content = <Tr>
          <Td colSpan="6" style={{ "padding": "2rem" }} className="font-size-16">
            <Spinner className="ms-2" color="primary" />
          </Td>
        </Tr>;
      } else {
        content = this.state.options.map((opt, index) => {
          var self = this;
          var num = index;
          return <Tbody key={index}>
            <Tr>
              <Td style={{ "padding": "2rem" }}>
                {opt.name}
              </Td>
              <Td style={{ "padding": "2rem" }}>
                <Input type="number" step={1} name="contracts" id="contracts" placeholder="Nº contratos" onChange={(e) => {this.changeContractNum(e.target.value, num)}}/>
              </Td>
              <Td style={{ "padding": "2rem" }}>
                {opt.exercise_price}
              </Td>
              <Td style={{ "padding": "2rem" }}>
                {opt.close_price}
              </Td>
              <Td style={{ "padding": "2rem" }}>
                {opt.type}
              </Td>
              <Td style={{ "padding": "2rem" }}>
                <Input className="form-select" type="select" name="transaction_type" id="transaction_type" onChange={(e) => {this.changeTransactionType(e.target.value, num)}}>
                  <option value="LONG">LONG</option>
                  <option value="SHORT">SHORT</option>
                </Input>
              </Td>
              <Td style={{ "padding": "2rem" }}>
                <Button color="primary" onClick={async function () {
                  self.modal_chart(index);
                }}>
                  <i className='bx bx-line-chart font-size-16 align-middle'></i>
                </Button>
                <Modal
                  size="lg"
                  isOpen={this.state.chartModal[index]}
                  toggle={() => {
                    //this.modal_chart()
                  }}
                  centered={true}
                >
                  <div className="modal-header">
                    <h5 className="modal-title mt-0">Opção</h5>
                    <button
                      type="button"
                      onClick={() => {
                        this.modal_chart(index)
                      }}
                      className="close"
                      data-dismiss="modal"
                      aria-label="Close"
                    >
                      <span aria-hidden="true">&times;</span>
                    </button>
                  </div>
                  <div className="modal-body">
                    {this.state.strategyData == null 
                      ? <div style={{ "textAlign": "center" }}><Spinner className="ms-2" color="primary" /></div>
                      : <OptsShortChart data={this.state.strategyData[index]} title={opt.name} />
                    }
                  </div>
                </Modal>
              </Td>
            </Tr>
          </Tbody>;
        }) //Retorna o content(tabela)
      } //Fim do else (strategyData != null)
    } //Fim do else (options.length == 0)

    if (this.state.strategyData === null || this.state.options.length == 0) {
      payoff = <div></div>;
    } else {
      var len = this.state.strategyData.length - 1;
      payoff = (
        <div>
          <h3>Payoff da Estratégia</h3>
          <Payoff data={this.state.strategyData[len]} />
        </div>
      );
    }

    return (
      <React.Fragment>
        <div className="page-content">
          <MetaTags>
            <title>Estratégias</title>
          </MetaTags>
          <Container fluid>
            <h4>Criar Estrutura de Operação</h4>
            <Row>
              <Col>
                <Card>
                  <CardBody>
                    <div>
                      <Col style={{ "textAlign": "center", "marginTop": "15px" }}>
                        <Row style={{ "justifyContent": "center" }}>
                          <Row>
                            <div style={{ "textAlign": "center", "marginBottom": "20px", "marginTop": "30px" }}><h4>Buscar Opções:</h4></div>
                          </Row>
                          <Row style={{ "justifyContent": "center" }}>
                            <Col xl={{ "size": "10" }}><SearchBar addOption={this.addOpt} /></Col>
                            <Col xl={{ "size": "2" }}>
                              <button
                                type="button"
                                className="btn btn-primary "
                                onClick={() => {
                                  this.modal_create_opt()
                                }}
                              >
                                <i className="bx bxs-send font-size-16 align-middle me-2" style={{ "color": "white" }}></i>{" "}
                                Criar Opção
                              </button>
                              <Modal
                                size="lg"
                                isOpen={this.state.modal_create_opt}
                                toggle={() => {
                                  modal_create_opt()
                                }}
                                centered={true}
                              >
                                <div className="modal-header">
                                  <h5 className="modal-title mt-0">Crie uma opção fictícia</h5>
                                  <button
                                    type="button"
                                    onClick={() => {
                                      this.modal_create_opt()
                                    }}
                                    className="close"
                                    data-dismiss="modal"
                                    aria-label="Close"
                                  >
                                    <span aria-hidden="true">&times;</span>
                                  </button>
                                </div>
                                <div className="modal-body">
                                  <Row>
                                    <Col xl={{ "size": "6" }}>
                                      <Input
                                        type="text"
                                        id="name"
                                        required
                                        placeholder="Nome"
                                      />
                                    </Col>
                                    <Col xl={{ "size": "3" }}>
                                      <Input
                                        type="select"
                                        className="form-select"
                                        id="option_type_fc"
                                        required
                                        placeholder="Tipo da opção"
                                      >
                                        <option value="CALL">CALL</option>
                                        <option value="PUT">PUT</option>
                                      </Input>
                                    </Col>
                                    <Col xl={{ "size": "3" }}>
                                      <Input
                                        type="select"
                                        className="form-select"
                                        id="transaction_type_fc"
                                        required
                                        placeholder="Tipo da transação"
                                      >
                                        <option value="LONG">LONG</option>
                                        <option value="SHORT">SHORT</option>
                                      </Input>
                                    </Col>
                                  </Row>

                                  <Row>{""}<br /></Row>

                                  <Row>
                                    <Col xl={{ "size": "4" }}>
                                      <Input
                                        type="number"
                                        step={1}
                                        id="contracts_fc"
                                        required
                                        placeholder="Contratos"
                                      />
                                    </Col>
                                    <Col xl={{ "size": "4" }}>
                                      <Input
                                        type="number"
                                        step={0.01}
                                        id="price_option"
                                        required
                                        placeholder="Preço (Opção)"
                                      />
                                    </Col>
                                    <Col xl={{ "size": "4" }}>
                                      <Input
                                        type="number"
                                        step={0.01}
                                        id="price_underlying"
                                        required
                                        placeholder="Preço (Underlying)"
                                      />
                                    </Col>
                                  </Row>

                                  <Row>{""}<br /></Row>

                                  <Row style={{ "justifyContent": "center" }}>
                                    <Col xl={{ "size": "4" }} style={{ "textAlign": "center" }}>
                                      <Button color="primary" onClick={() => { 
                                        var obj = {
                                          name: document.getElementById("name").value,
                                          id: "",
                                          exercise_price: parseInt(document.getElementById("price_option").value),
                                          close_price: parseInt(document.getElementById("price_underlying").value),
                                          type: document.getElementById("option_type_fc").value,
                                          contracts: parseInt(document.getElementById("contracts_fc").value),
                                          transaction_type: document.getElementById("transaction_type_fc").value,
                                        }
                                        this.addOpt(obj); 
                                      }}>Adicionar</Button>
                                    </Col>
                                  </Row>
                                </div>
                              </Modal>
                            </Col>
                          </Row>

                        </Row>
                        <Row>
                          <Table>
                            <Thead>
                              <Tr style={{ "backgroundColor": "#081E30", "color": "white" }}>
                                <Th>Nome</Th>
                                <Th>Número de contratos</Th>
                                <Th>{"Preço(Opção)"}</Th>
                                <Th>{"Preço(Underlying)"}</Th>
                                <Th>{"Tipo(Opção)"}</Th>
                                <Th>{"Tipo(Transação)"}</Th>
                                <Th></Th>
                              </Tr>
                            </Thead>
                            {content}
                          </Table>
                        </Row>
                        <Row>{payoff}</Row>
                        <br />
                        {this.state.options.length > 0 
                          ? this.state.isCreated == true
                            ? (<Row style={{ "justifyContent": "center" }}>
                              <Col xl={{ "size": "4" }}>
                                <Button color="primary" onClick={() => {
                                  this.updateStrategy()
                                }}>
                                  <i className='bx bxs-send font-size-20 align-middle me-2' style={{ "color": "white" }}></i>{" "}
                                  Atualizar Operação
                                </Button>
                              </Col>
                              <Col xl={{ "size": "2" }} id="shareBtn">
                                <Button color="primary" onClick={() => {
                                  this.shareStrategy()
                                }}>
                                  <i className='bx bxs-share-alt font-size-20 align-middle me-2' style={{ "color": "white" }}></i>{" "}
                                  Compartilhar
                                </Button>
                              </Col>
                            </Row>)
                            : (<Row style={{ "justifyContent": "center" }}>
                              <Col xl={{ "size": "4" }}>
                                <Input type="text" id="strategy_name" required placeholder="Nome da estratégia" />
                              </Col>
                              <Col xl={{ "size": "4" }}>
                                <Button color="primary" onClick={() => {
                                  document.getElementById("strategy_name").value === "" 
                                    ? toastr.error("É necessário informar um nome para criar a estratégia") 
                                    : this.createStrategy(document.getElementById("strategy_name").value);
                                }}>
                                  <i className='bx bxs-send font-size-20 align-middle me-2' style={{ "color": "white" }}></i>{" "}
                                  Criar Operação
                                </Button>
                              </Col>
                            </Row>) 
                          : (<Row></Row>)}
                      </Col>
                    </div>
                  </CardBody>
                </Card>
              </Col>
            </Row>
          </Container>
        </div>
      </React.Fragment >
    );
  }
}

export default Strategies;