import React, { Component } from "react";
import Loading from "components/CommonForBoth/Loading";
import MetaTags from "react-meta-tags";
import PropTypes from "prop-types";
import { Row, Col, Card, CardBody, CardTitle, Container, Spinner, } from "reactstrap";
import { withRouter } from 'react-router-dom';
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
      data: null,
      name: this.props.location.state.name,
      id: this.props.location.state.id,
    };
  }

  async componentDidMount() {
    const self = this;
    console.log(`Name:${self.state.name.replace(/ /g, '')}, ID.:${self.state.id.replace(/ /g, '')}`);

    var raw = JSON.stringify({
      "name": self.state.name,
      "id": self.state.id
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
    //Condicional de envio de dados para o gráfico
    let renderContent;
    if (this.state.data == null) {
      renderContent = <div style={{"textAlign": "center"}}><Spinner className="ms-2" color="primary" /></div>;
    } else {
      //Dados iniciais da Option
      let optInfo = {
        "name": this.state.data.name,
        "type": this.state.data.type,
        "exercise_price": this.state.data.exercise_price,
        "currency": this.state.data.currency,
        "expiration_date": this.state.data.expiration_date,
        "name_underlying": this.state.data.name_underlying,
        "expiration_time": this.state.data.expiration_time,
      }
      renderContent = <div>
        <CardTitle className="mb-1">
          {this.state.data.name}
        </CardTitle>
        <Row>
          <OptionsClose data={this.state.data.option_close_series} info={optInfo} />
        </Row>
        <Row>
          <GreekTable data={this.state.data.greeks} name={this.state.data.name} />
        </Row>
        <Row>
          <PriceTable data={this.state.data.price} />
        </Row>
        <Row>
          <MarketTable data={this.state.data.market} />
        </Row>
        <Row>
          <OptsShortChart data={this.state.data.payoff[0]} />
        </Row>
        <Row>
          <OptionsLong data={this.state.data.payoff} />
        </Row>
      </div>
    }

    return (
      <React.Fragment>
        <div className="page-content">
          <MetaTags>
            <title>Opções</title>
          </MetaTags>
          <Container fluid>
            <Row>
              <Col>
                <Card>
                  <CardBody >
                    {renderContent}
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

Opts.propTypes = {
  location: PropTypes.object,
}

export default withRouter(Opts)