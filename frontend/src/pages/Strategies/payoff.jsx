import React, { Component } from "react";
import PropTypes from "prop-types";
import { Row, Col, Card, CardBody } from "reactstrap";
import { Table, Thead, Tbody, Tr, Th, Td } from "react-super-responsive-table";
import ReactApexChart from "react-apexcharts";

class Payoff extends Component {
    constructor(props) {
        super(props);
        this.state = {}
    }

    render() {
        var series = [
            {
                name: "Lucro / Prejuízo",
                data: this.props.data.y.map(p => p.toFixed(4)),
            },
        ];
        var options = {
            chart: {
                toolbar: "false",
            },
            legend: {
                show: true,
                position: 'top',
            },
            labels: this.props.data.x,
            colors: ["#FF6347"],
            stroke: {
                curve: "smooth",
                width: 3,
            },
            xaxis: {
                show: true,
                title: {
                    text: 'Preço do ativo base (R$)'
                }
            },
            yaxis: {
                show: true,
                title: {
                    text: 'Lucro / Prejuízo (R$)'
                }
            }
        };

        return (
            <>
                <Col xl="12">
                    <Card>
                        <CardBody>
                            <Row>
                                <Col lg="12">
                                    <div id="line-chart" className="apex-charts" dir="ltr">
                                        <ReactApexChart
                                            series={series}
                                            options={options}
                                            type="line"
                                            height={320}
                                            className="apex-charts"
                                        />
                                    </div>
                                </Col>
                            </Row>
                        </CardBody>
                    </Card>
                </Col>
            </>
        );
    }
}

Payoff.propTypes = {
    data: PropTypes.object,
}

export default Payoff;