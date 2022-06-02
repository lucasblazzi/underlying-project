import React, { Component } from "react";
import MetaTags from "react-meta-tags";
import {Row, Col, Card, CardBody, CardImg, Container, Input, Button, Table} from "reactstrap";
import logo from "../../assets/images/logo-underlying.png";
import { Link } from "react-router-dom";

class Search extends Component {
  constructor(props) {
    super(props);
    this.state = {
      busca: "",
      loading: false,
      result: []
    }
    this.timeout = 0;
  }

  search(requestOptions) {
      this.setState({loading: true})
      fetch("https://lgbxzn9a97.execute-api.us-east-1.amazonaws.com/v1/search", requestOptions)
          .then(response => response.json())
          .then(result => {
            console.log(result);
            this.setState({result: result, loading: false});
          })
          .catch(error => console.log('error', error));
    }

  onChangeHandler(e) {
    var requestOptions = {
      method: 'POST',
      body: JSON.stringify({
        "query": e.target.value
      }),
      redirect: 'follow'
    };
    if(this.timeout) clearTimeout(this.timeout);
    this.timeout = setTimeout(() => {
      this.search(requestOptions);
      this.setState({ busca: e.target.value });
    }, 700);
  };

  renderOptions(){
    let result = "There's no movies";
    if (this.state.result) {
      console.log(this.state.result);
    }
    return result;
  }

  render() {
    return (
      <React.Fragment>
        <div className="page-content">
          <MetaTags>
            <title>Pesquisa</title>
          </MetaTags>
          <Container fluid>
            <Row >
              <Col style={{ "textAlign": "center", }}>
                <CardImg style={{
                  "width": "50%",
                  "height": "80%",
                }} height={"100vh"} src={logo} alt="Underlying Logo" />
                <Row style={{ "justifyContent": "center" }}>
                  <Col xl={{ "size": "6" }}>
                    <Input
                      type="text"
                      id="busca"
                      required
                      onChange={(e) => this.onChangeHandler(e)}
                    />
                  </Col>
                </Row>
              </Col>
              <Row style={{ "justifyContent": "center" }}>
                  <div className="table-responsive">
                    <Table className="table align-middle table-nowrap">
                        <tbody>
                        {this.state.result.map((element, index) => (
                            <tr key={index}>
                                <td>
                                    <div>
                                        <h5 className="font-size-14 mb-1">{element.name} | {element.name_underlying}</h5>
                                        <p className="text-muted mb-0">Data: {element.date} |
                                            Vencimento: {element.expiration_date}</p>
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
                                            Preço de fechamento: {element.close_price} | Preço de
                                            exercício: {element.exercise_price}
                                        </h5>
                                    </div>
                                </td>

                                <td>
                                    <div className="text-end">
                                        <h5 className="font-size-20 mb-0">
                                            <Link to={{pathname: "../opts", state: {name: element.name, id: element.id}}}
                                                  style={{"border": "none"}}>
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
                </Row>
            </Row>
          </Container>
        </div>
      </React.Fragment>
    );
  }
}

export default Search;