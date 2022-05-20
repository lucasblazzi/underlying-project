import React, { Component } from "react";
import PropTypes from "prop-types";
import { Row, Col, Card, CardBody } from "reactstrap";
import ReactApexChart from "react-apexcharts";

class PriceChart extends Component {
    constructor(props) {
        super(props);
        this.state = {
            series: [
                {
                    name: "series1",
                    data: this.props.data.x,
                },
            ],
            options: {
                chart: {
                    toolbar: "false",
                },
                dataLabels: {
                    enabled: !1,
                },
                labels: this.props.data.payoff,
                colors: ["#50b0eb"],
                stroke: {
                    curve: "smooth",
                    width: 3,
                },
            },
        }
    }

    render() {
        return (
            <>
                <Col xl="12">
                    <Card>
                        <CardBody>
                            <div className="clearfix">
                                <h4 className="card-title mb-4">Gráfico de preços</h4>
                            </div>
                            <Row>
                                <Col lg="12">
                                    <div id="line-chart" className="apex-charts" dir="ltr">
                                        <ReactApexChart
                                            series={this.state.series}
                                            options={this.state.options}
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

PriceChart.propTypes = {
    data: PropTypes.object,
}

export default PriceChart;