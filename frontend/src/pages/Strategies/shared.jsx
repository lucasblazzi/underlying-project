import React, { Component } from "react";
import MetaTags from "react-meta-tags";
import { Row, Col, Card, CardBody, CardTitle, Container, Media, TabPane, Spinner } from "reactstrap";
import PropTypes from "prop-types";

class SharedStrategies extends Component {
    constructor(props) {
        super(props);
        this.state = {
            sharedStrts: null,
        };
    }
  
    componentDidMount() {
        var raw = JSON.stringify({});

        var requestOptions = {
        method: 'POST',
        body: raw,
        redirect: 'follow'
        };

        fetch("https://jdmgjcpm1m.execute-api.us-east-1.amazonaws.com/v1/shared", requestOptions)
        .then(response => response.json())
        .then(result => {
            this.setState({ sharedStrts: result });
            console.log(result)
        })
        .catch(error => console.log('error', error));
    }
  
    render() {
        var content;
        if (this.state.sharedStrts === null) { 
            content = <div style={{ "textAlign": "center" }}><Spinner className="ms-2" color="primary" /></div>;
        } else {
            content = this.state.sharedStrts.map((strt, index) => {
                return (
                    <Card 
                        key={index}
                        onClick={this.routingFunction = () => {
                            this.props.history.push({
                                pathname: '/view-strategy',
                                state: { name: strt.name, username: strt.username, strategy: strt.strategy },
                            });
                        }}
                        style={{ cursor: "pointer" }}
                    >
                      <CardBody>
                        <h4>{strt.name}</h4>
                        {strt.username}
                      </CardBody>
                    </Card>
                )
            });
        }
        return (
        <React.Fragment>
            <div className="page-content">
            <MetaTags>
                <title>Estratégias compartilhadas</title>
            </MetaTags>
            <Container fluid>
                <h4>Estratégias compartilhadas</h4>
                <Row>
                <Col>
                    <Card>
                    <CardBody>
                        {content}
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

SharedStrategies.propTypes = {
    history: PropTypes.any,
}

export default SharedStrategies;