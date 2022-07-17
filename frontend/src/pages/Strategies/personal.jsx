import React, { Component } from "react";
import MetaTags from "react-meta-tags";
import { Row, Col, Card, CardBody, CardTitle, Container, Media, TabPane, Spinner, Button } from "reactstrap";
import PropTypes from "prop-types";
import { Link } from "react-router-dom";

class PersonalStrategies extends Component {
    constructor(props) {
        super(props);
        this.state = {
            myStrts: null,
        };
    }

    componentDidMount() {
        var user = localStorage.getItem("logedUser");
        var raw = JSON.stringify({
            "username": user
        });

        var requestOptions = {
            method: 'POST',
            body: raw,
            redirect: 'follow'
        };

        fetch("https://jdmgjcpm1m.execute-api.us-east-1.amazonaws.com/v1/user", requestOptions)
            .then(response => response.json())
            .then(result => {
                this.setState({ myStrts: result });
                console.log(result)
            })
            .catch(error => console.log('error', error));
    }

    render() {
        var content;
        if (this.state.myStrts === null) {
            content = <div style={{ "textAlign": "center" }}><Spinner className="ms-2" color="primary" /></div>;
        } else {
            if (this.state.myStrts.length === 0) {
                content = <div style={{ "textAlign": "center" }}>
                    <h3>Nenhuma estratégia registrada!</h3>
                    <Link
                        className="nav-link dropdown-toggle arrow-none"
                        to="/strategies"
                    >
                        <Button color="info" onClick={() => { null }}>Criar estratégia</Button>
                    </Link>
                </div>;
            } else {
                content = this.state.myStrts.map((strt, index) => {
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

PersonalStrategies.propTypes = {
    history: PropTypes.any,
}

export default PersonalStrategies;