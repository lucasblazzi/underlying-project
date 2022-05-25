import React, { Component } from "react";
import PropTypes from "prop-types";
import { Row, Col, Card, CardBody } from "reactstrap";
import ReactApexChart from "react-apexcharts";

class OptionsClose extends Component {
    constructor(props) {
        super(props);
        console.log(this.props.data) 
        
        const seriesData = [];
        const options = {}

        this.props.data.map((val) => {
            seriesData.push(
            {
                x: val.date,   //
                y: val.value  //
            }
            );
        });

        this.state = {
            series: [
                {
                    name: "optionsClose",
                    data: seriesData,
                },
            ],
            options: {
                chart: {
                    toolbar: "false",
                },
                dataLabels: {
                    enabled: !1,
                },
                labels: {},
                colors: seriesData[0] < seriesData[length - 1] ? ["#50b0eb"] : ["#ff2400"],
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
                                <h4 className="card-title mb-4">Opções fechadas</h4>
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

OptionsClose.propTypes = {
    data: PropTypes.array,
}

export default OptionsClose;