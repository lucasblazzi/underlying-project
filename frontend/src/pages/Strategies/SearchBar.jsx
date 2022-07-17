import React, { Component } from "react"
import MetaTags from "react-meta-tags"
import {
  Row,
  Col,
  Card,
  CardBody,
  CardImg,
  Container,
  Input,
  Button,
  Table,
  Spinner,
  InputGroup,
  InputGroupAddon,
  Dropdown,
} from "reactstrap"
import "../Search/dots.css"
import InfiniteScroll from "react-infinite-scroll-component"
import PropTypes from "prop-types"
import SimpleBar from "simplebar-react"

class SearchBar extends Component {
  constructor(props) {
    super(props)
    this.state = {
      busca: "",
      loading: false,
      result: null,
      count: 0,
      drop: false,
      open: true,
    }
    this.timeout = 0
    this.renderOptions = this.renderOptions.bind(this)
  }

  search(requestOptions) {
    this.setState({ loading: true })
    fetch(
      "https://lgbxzn9a97.execute-api.us-east-1.amazonaws.com/v1/search",
      requestOptions
    )
      .then(response => response.json())
      .then(result => {
        console.log(result)
        this.setState({
          result: this.state.result.concat(result),
          loading: false,
        })
      })
      .catch(error => console.log("error", error))
  }

  onChangeHandler(e) {
    this.setState({ result: [] })
    this.setState({ count: 0 })
    var requestOptions = {
      method: "POST",
      body: JSON.stringify({
        query: e.target.value,
        from: 0,
        size: 10,
      }),
      redirect: "follow",
    }
    if (this.timeout) clearTimeout(this.timeout)

    document.getElementById("load").hidden = false

    this.timeout = setTimeout(() => {
      this.search(requestOptions)
      this.setState({ busca: e.target.value })
      document.getElementById("load").hidden = true
    }, 700)
  }

  renderOptions() {
    var self = this
    var next = self.state.count + 10
    var value = document.getElementById("busca").value
    //console.log("Busca value = ", value);
    var requestOptions = {
      method: "POST",
      body: JSON.stringify({
        query: value,
        from: next,
        size: 10,
      }),
      redirect: "follow",
    }

    if (self.timeout) clearTimeout(self.timeout)
    self.timeout = setTimeout(() => {
      self.search(requestOptions)
      self.setState({ busca: value, count: next })
    }, 700)
  }

  render() {
    var resultContent
    if (this.state.result == null || this.state.result.length == 0) {
      resultContent = <div></div>
    } else {
      this.setState(prevState => {
        if(prevState.open != true) {
          return { open: true }
        }
      })                             
      this.state.busca == ""
        ? (resultContent = <div></div>)
        : (resultContent = (
            <Dropdown
                isOpen={this.state.open}
                className="dropdown d-inline-block"
                style={{"width": "50vw"}}
            >
              <InfiniteScroll
                dataLength={this.state.result.length}
                next={this.renderOptions}
                hasMore={true}
              >
                <SimpleBar style={{ "maxHeight": "630px" }}>
                <div
                  className="table-responsive"
                  style={{
                    // "position": "absolute",
                    // "zIndex": "1",
                    "backgroundColor": "whitesmoke",
                    "overflow": "scroll",
                  }}
                >
                  <Table className="table align-middle table-nowrap">
                    <tbody>
                      {this.state.result.map((element, index) => (
                        <tr
                          key={index}
                          style={{ cursor: "pointer" }}
                          onClick={() => {
                            var obj = {
                              name: element.name,
                              id: element.id,
                              exercise_price: element.exercise_price,
                              close_price: element.close_price,
                              type: element.type,
                              contracts: 1,
                              transaction_type: "LONG",
                            }
                            //console.log("Clicado:", obj)
                            //Para cada opção, fazer a requisição e guardar num array?
                            // var requestOptions = {
                            //   method: "POST",
                            //   body: obj,
                            //   redirect: "follow",
                            // }

                            // fetch(
                            //   "https://lgbxzn9a97.execute-api.us-east-1.amazonaws.com/v1/info",
                            //   requestOptions
                            // )
                            //   .then(response => response.json())
                            //   .then(result => {
                            //     var resObj = {
                            //       name: result.name,
                            //       exercise_price: result.exercise_price,
                            //       transaction_type: "LONG",
                            //       close_price: 1.23,
                            //       contracts: 1,
                            //       type: result.type,
                            //     }
                            //   })
                            //   .catch(error => console.log("error", error))
                            this.props.addOption(obj)
                            document.getElementById("busca").value = ""
                            this.setState({ open: false })
                            this.setState({ busca: "" })
                            resultContent = <div></div>
                          }}
                        >
                          <td>
                            <div>
                              <h5 className="font-size-14 mb-1">
                                {element.name} | {element.name_underlying} |{" "}
                                {element.type}
                              </h5>
                              <p className="text-muted mb-0">
                                Data: {element.date} | Vencimento:{" "}
                                {element.expiration_date}
                              </p>
                            </div>
                          </td>

                          <td>
                            <div className="text-end">
                              <h5 className="font-size-14 text-muted mb-0">
                                Preço de fechamento: {element.close_price}
                                <br />
                                Preço de exercício: {element.exercise_price}
                              </h5>
                            </div>
                          </td>
                        </tr>
                      ))}
                    </tbody>
                  </Table>
                </div>
                </SimpleBar>
              </InfiniteScroll>
            </Dropdown>
          ))
    }
    return (
      <>
        <Row>
          <Col xl={{ size: "12" }}>
            <Input
              type="text"
              id="busca"
              required
              onChange={e => this.onChangeHandler(e)}
              placeholder="Buscar..."
              style={{ marginBottom: "2rem" }}
            >
              <i className="bx bx-search me-2"></i>
            </Input>
          </Col>

          {/* Loading de pesquisa */}
          <Row id="load" hidden>
            <Col
              xl={{ size: 8, offset: 6 }}
              md={{ size: 8, offset: 6 }}
              sm="12"
            >
              <div className="dot-flashing mt-2"></div>
            </Col>
          </Row>
          {/* FIM Loading de pesquisa */}

          {/* Resultado da pesquisa */}
          <Row style={{ justifyContent: "center" }}>
            <Col xl={{ size: "8" }}>{resultContent}</Col>
          </Row>
          {/* FIM Resultado da pesquisa */}
        </Row>
      </>
    )
  }
}

SearchBar.propTypes = {
  history: PropTypes.any,
  addOption: PropTypes.func,
}

export default SearchBar