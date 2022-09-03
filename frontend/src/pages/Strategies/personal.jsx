import React, { Component } from "react"
import MetaTags from "react-meta-tags"
import {
  Row,
  Col,
  Card,
  CardBody,
  CardTitle,
  Container,
  Media,
  Table,
  Spinner,
  Button,
} from "reactstrap"
import PropTypes from "prop-types"
import { Link } from "react-router-dom"
import Swal from "sweetalert2"
import toastr from "toastr"
import withReactContent from "sweetalert2-react-content"

class PersonalStrategies extends Component {
  constructor(props) {
    super(props)
    this.state = {
      myStrts: null,
      MySwal: withReactContent(Swal),
    }
    this.sweetalert = this.sweetalert.bind(this)
    this.deleteStrategy = this.deleteStrategy.bind(this)
    this.getStrategies = this.getStrategies.bind(this)
    this.share = this.share.bind(this)
  }

  sweetalert(id) {
    Swal.fire({
      title: "Deletar estratégia?",
      icon: "warning",
      showCancelButton: true,
      confirmButtonColor: "#3085d6",
      cancelButtonColor: "#d33",
      confirmButtonText: "Sim, deletar!",
      cancelButtonText: "Não, cancelar!",
      allowOutsideClick: false,
    }).then(async result => {
      if (result.isConfirmed) {
        var confirm = await this.deleteStrategy(id)
        Swal.fire("Deletado!", "A estratégia foi removida.", "success")
            .then(async () => {
                await this.getStrategies()
            })
      } else if (!result.isConfirmed) {
        Swal.fire("Cancelado", "Sua estratégia continua", "error")
      }
    })
  }

  async deleteStrategy(id) {
    var raw = JSON.stringify({
      id: id,
      "deleted": true
    })

    var requestOptions = {
      method: "POST",
      body: raw,
      redirect: "follow",
    }

    fetch(
      "https://jdmgjcpm1m.execute-api.us-east-1.amazonaws.com/v1/delete",
      requestOptions
    )
      .then(response => response.json())
      .then(result => {
        console.log("Excluído:", result)
        toastr.success("", "A estratégia foi excluída com sucesso!")
      })
      .catch(error => {
        console.log("Erro:", error)
        toastr.error("Erro", "A estratégia não foi excluída!")
      })
  }

  async getStrategies() {
    var user = localStorage.getItem("logedUser")
    var raw = JSON.stringify({
      username: user,
    })

    var requestOptions = {
      method: "POST",
      body: raw,
      redirect: "follow",
    }

    fetch(
      "https://jdmgjcpm1m.execute-api.us-east-1.amazonaws.com/v1/user",
      requestOptions
    )
      .then(response => response.json())
      .then(result => {
        this.setState({ myStrts: result })
        console.log(result)
      })
      .catch(error => console.log("error", error))
  }

  share(id) {
    var requestOptions = {
        method: 'POST',
        body: JSON.stringify({ id: id, shared: true }),
        redirect: 'follow'
    };
    fetch("https://jdmgjcpm1m.execute-api.us-east-1.amazonaws.com/v1/share", requestOptions)
        .then(response => response.json())
        .then(result => {
            toastr.success("", "Estratégia compartilhada com sucesso!")
        })
        .catch(error => {
            console.log('error', error)
            toastr.error("Erro", "A estratégia não foi compartilhada!")
        });
  }

  async componentDidMount() {
    await this.getStrategies()
  }

  render() {
    var content
    if (this.state.myStrts === null) {
      content = (
        <div style={{ textAlign: "center" }}>
          <Spinner className="ms-2" color="primary" />
        </div>
      )
    } else {
      if (this.state.myStrts.length === 0) {
        content = (
          <div style={{ textAlign: "center" }}>
            <h3>Nenhuma estratégia registrada!</h3>
            <Link
              className="nav-link dropdown-toggle arrow-none"
              to="/strategies"
            >
              <Button
                color="info"
                onClick={() => {
                  null
                }}
              >
                Criar estratégia
              </Button>
            </Link>
          </div>
        )
      } else {
        content = this.state.myStrts.map((strt, index) => {
          return (
            <Row key={index}>
              <Col
                lg="12"
                onClick={
                  (this.routingFunction = () => {
                    this.props.history.push({
                      pathname: "/view-strategy",
                      state: {
                        name: strt.name,
                        username: strt.username,
                        strategy: strt.strategy,
                      },
                    })
                  })
                }
                style={{ cursor: "pointer" }}
              >
                <Card>
                  <CardBody>
                    <Row>
                      <Col lg="9">
                        <h4>{strt.name}</h4>
                        {strt.username}
                      </Col>
                      {strt.shared == false 
                        ? <Col lg="1">
                        <button
                          id={"btn"+index}
                          type="button"
                          className="btn btn-light"
                          onClick={event => {
                            event.stopPropagation()
                            this.share(strt.id)
                            document.getElementById("btn"+index).hidden = "display: none"
                          }}
                        >
                          <i className='bx bxs-share'></i>
                        </button>
                      </Col>
                      : <Col lg="1">
                            <button type="button"
                                className="btn btn-light" 
                                onClick={()=>{null}} 
                                style={{"backgroundColor":"rgba(0, 0, 0, 0)", "borderStyle": "none" }}>
                            </button>
                      </Col>
                    }
                      <Col lg="1"
                        onClick={(event) => {
                            event.stopPropagation()
                        }}
                      >
                            <button
                            type="button"
                            className="btn btn-light"
                            onClick={(this.routingFunction = () => {
                                this.props.history.push({
                                  pathname: "/edit-strategy",
                                  state: {
                                    name: strt.name,
                                    id: strt.id,
                                    strategy: strt.strategy,
                                  },
                                })
                              })}
                            >
                            {" "}
                            <i className="bx bxs-edit-alt"></i>
                            </button>
                      </Col>
                      <Col lg="1">
                        <button
                          type="button"
                          className="btn btn-light"
                          onClick={event => {
                            event.stopPropagation()
                            this.sweetalert(strt.id)
                          }}
                        >
                          <i className="bx bxs-trash"></i>
                        </button>
                      </Col>
                    </Row>
                  </CardBody>
                </Card>
              </Col>
            </Row>
          )
        })
      }
    }
    return (
      <React.Fragment>
        <div className="page-content">
          <MetaTags>
            <title>Minhas estratégias</title>
          </MetaTags>
          <Container fluid>
            <h4>Minhas estratégias</h4>
            <Row>
              <Col>
                <Card>
                  <CardBody>{content}</CardBody>
                </Card>
              </Col>
            </Row>
          </Container>
        </div>
      </React.Fragment>
    )
  }
}

PersonalStrategies.propTypes = {
  history: PropTypes.any,
}

export default PersonalStrategies
