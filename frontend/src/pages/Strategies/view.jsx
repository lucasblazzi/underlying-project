import React, { Component } from "react";
import MetaTags from "react-meta-tags";
import PropTypes from "prop-types";
import { Row, Col, Card, CardBody, CardTitle, Container, Spinner } from "reactstrap";
import { withRouter } from 'react-router-dom';
import OptsShortChart from "pages/Opts/OptsShortChart";
import Payoff from "./payoff";

class ViewStrategy extends Component {
    constructor(props) {
        super(props);
        this.state = {
            strategyData: null,
        };
    }
    componentDidMount() {
        var { strategy } = this.props.location.state;

        var bodyRaw = JSON.stringify({ "strategy": strategy })
        var requestOptions = {
            method: 'POST',
            body: bodyRaw,
            redirect: 'follow'
          };
          
        fetch("https://jdmgjcpm1m.execute-api.us-east-1.amazonaws.com/v1/payoff", requestOptions)
        .then(response => response.json())
        .then(result => {
            this.setState({ strategyData: result });
            console.log(result)
        })
        .catch(error => console.log('error', error));
    }

    render() {
        var { name, username } = this.props.location.state;
        var content;

        if(this.state.strategyData == null) {
            content = <div style={{ "textAlign": "center" }}><Spinner className="ms-2" color="primary" /></div>;
        } else {
            // content = <div></div>;
            var len = this.state.strategyData.length;
            // for(var i = 0; i < len - 1; i++) { 
            //     content += <OptsShortChart data={this.state.strategyData[i]} title=""/>
            // }
            // content += <Payoff data={this.state.strategyData[len - 1]} title=""/>
            
            content = this.state.strategyData.map((strt, index) => {
                if(index != len - 1) {
                    return <div key={index}>
                        <OptsShortChart data={strt} title=""/>
                    </div>
                } else {
                    return <div key={index}>
                        <div className="mt-5" style={{"textAlign": "center"}}><h3>Payoff da Estratégia</h3></div>
                        <Payoff data={strt} />
                    </div>
                }
            })
        }

        return (
            <React.Fragment>
                <div className="page-content">
                    <MetaTags>
                        <title>{name}</title>
                    </MetaTags>
                    <Container fluid>
                        <h4>{name}</h4>
                        <Row>
                            <Col>
                                <Card>
                                    <div className="m-3">
                                        <h5>Usuário: {username}</h5>
                                    </div>
                                    {content}
                                </Card>
                            </Col>
                        </Row>
                    </Container>
                </div>
            </React.Fragment>
        );
    }
}

ViewStrategy.propTypes = {
    location: PropTypes.object,
}

export default withRouter(ViewStrategy);