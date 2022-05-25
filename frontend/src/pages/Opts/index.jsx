import Loading from "components/CommonForBoth/Loading";
import { post } from "helpers/api_helper";
import React, { Component } from "react";
import MetaTags from "react-meta-tags";
import { Row, Col, Card, CardBody, CardTitle, Container, } from "reactstrap";
import GreekTable from "./GreekTable";
import PriceChart from "./PriceChart";
import PriceTable from "./PriceTable";
import MarketTable from "./MarketTable";
import OptionsClose from "./OptionsClose";
import OptionsLong from "./OptionsLong"
import OptsShortChart from "./OptsShortChart";

class Opts extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: {},
    };
  }

  async componentDidMount() {
    const self = this;

    var raw = JSON.stringify({
      "name": "IBOVA100",
      "id": "ecd11825897a643f67c3d34c3569ee5b"
    });

    var requestOptions = {
      method: 'POST',
      body: raw,
      redirect: 'follow'
    };

    fetch("https://lgbxzn9a97.execute-api.us-east-1.amazonaws.com/v1/info", requestOptions)
      .then(response => response.json())
      .then(result => {
        self.setState({ data: result });
        //console.log(result);
      })
      .catch(error => console.log('error', error));

  }

  render() {
    //Spinning de load
    let loading = <Loading />

    //Condicional de envio de dados para o gráfico
    let optionCloseData = this.state.data.option_close_series == null
    ? loading
    : <OptionsClose data={this.state.data.option_close_series} />

    let optionsLongData = this.state.data.payoff == null
    ? loading
    : <OptionsLong data ={this.state.data.payoff}/>

     let shortChart = this.state.data.payoff == null
    ? loading
    : <OptsShortChart data={this.state.data.payoff[0]}/>
        
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
                      <CardTitle className="mb-1">
                        {this.state.data.name}
                      </CardTitle>
                      <Row>
                        <GreekTable data={this.state.data.greeks} name={this.state.data.name} />
                      </Row>
                      <Row>
                        {shortChart}
                      </Row>
                      <Row>
                        {optionsLongData}
                      </Row>
                      <Row>
                        <PriceTable data={this.state.data.price} />
                      </Row>
                      <Row>
                        <MarketTable data={this.state.data.market} />
                      </Row>
                      <Row>
                        {optionCloseData} 
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