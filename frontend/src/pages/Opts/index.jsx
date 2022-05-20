import Loading from "components/CommonForBoth/Loading";
import React, { Component } from "react";
import MetaTags from "react-meta-tags";
import { Row, Col, Card, CardBody, CardTitle, Container, } from "reactstrap";
import GreekTable from "./GreekTable";
import PriceChart from "./PriceChart";
import PriceTable from "./PriceTable";

class Opts extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: {},
    };
  }

  async componentDidMount() {
    const self = this;

    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    var raw = JSON.stringify({
      "name": "PETRF268",
      "id": "f794464f071ec41e48f16941563b3b0c"
    });

    var requestOptions = {
      method: 'POST',
      headers: myHeaders,
      body: raw,
      redirect: 'follow'
    };

    fetch("https://lgbxzn9a97.execute-api.us-east-1.amazonaws.com/v1/info", requestOptions)
      .then(response => response.json())
      .then(result => self.setState({ data: result }))
      .catch(error => console.log('error', error));

  }

  render() {
    //Spinning de load
    let loading = <Loading />

    //Condicional de envio de dados para o gráfico
    let priceChartData = this.state.data.greeks == null
      ? loading
      : <PriceChart data={this.state.data.payoff.strategy} />
    return (
      <React.Fragment>
        <div className="page-content">
          <MetaTags>
            <title>Opções</title>
          </MetaTags>
          <Container fluid>
            <h4>Opção</h4>
            <Row>
              <Col>
                <Card>
                  <CardBody>
                    <div>
                      <Row>
                        <GreekTable data={this.state.data.greeks} id={this.state.data.id} />
                      </Row>
                      <Row>
                        {priceChartData}
                      </Row>
                      <Row>
                        <PriceTable data={this.state.data.price} />
                      </Row>
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

export default Opts