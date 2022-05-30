import React, { Component } from "react";
import MetaTags from "react-meta-tags";
import { Row, Col, Card, CardBody, CardImg, Container, Input, Button } from "reactstrap";
import logo from "../../assets/images/logo-underlying.png";
import { Link } from "react-router-dom";

class Search extends Component {
  constructor(props) {
    super(props);
    this.state = {
      busca: "",
    }

    this.handleInputChange = this.handleInputChange.bind(this);
    this.submit = this.submit.bind(this);
  }

  handleInputChange(event) {
    const value = event.target.value;

    this.setState({
      busca: value,
    });
  }

  submit() {
    console.log(this.state.busca);
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
                      onChange={(e) => this.handleInputChange(e)}
                    />
                  </Col>
                  <Col xl={2} style={{ "textAlign": "center" }}>
                    <Link to={{
                      pathname: "../search-result",
                      state: { busca: this.state.busca }
                    }} >
                      <Button color="primary" onClick={(e) => this.submit()}>
                        <i className='bx bx-search font-size-16 align-middle'></i>{" "}
                        Pesquisar
                      </Button>
                    </Link>
                  </Col>
                </Row>
              </Col>
            </Row>
          </Container>
        </div>
      </React.Fragment>
    );
  }
}

export default Search;