import React, { Component } from "react";
import PropTypes from "prop-types";
import { Row, Col, Card, CardBody } from "reactstrap";
import { Table, Thead, Tbody, Tr, Th, Td } from "react-super-responsive-table";
import ReactApexChart from "react-apexcharts";

class OptionsClose extends Component {
    constructor(props) {
        super(props);
        //console.log(this.props.data)

        var seriesData = [];
        const options = {}

        this.props.data.map((val) => {
            if (val.transaction_type == "LONG") {
                seriesData = val
            }
        });

        this.state = {
            series: [
                {
                    name: "Lucro / Prejuízo",
                    data: seriesData.y,
                },
            ],
            options: {
                chart: {
                    toolbar: "false",
                },
                dataLabels: {
                    enabled: !1,
                },
                labels: seriesData.x,
                colors: ["#50b0eb"],
                stroke: {
                    curve: "smooth",
                    width: 3,
                },
            },
        }
    }

    render() {
        let tableContent;
        let tableValues = this.props.data[1];
        if (this.props.data != null) {
            tableContent = <Table
                id="short"
                className="table table-striped table-bordered"
            >
                <Thead>
                    <Tr>

                    </Tr>
                </Thead>
                <Tbody>
                    <Tr>
                        <Td>Preço de exercício</Td>
                        <Td>{tableValues.exercise_price}</Td>
                    </Tr>
                    <Tr>
                        <Td>Nome</Td>
                        <Td>{tableValues.name}</Td>
                    </Tr>
                    <Tr>
                        <Td>Preço de fechamento</Td>
                        <Td>{tableValues.close_price}</Td>
                    </Tr>
                    <Tr>
                        <Td>Número de papéis</Td>
                        <Td>{tableValues.contracts}</Td>
                    </Tr>
                    <Tr>
                        <Td>Tipo da opção</Td>
                        <Td>{tableValues.type}</Td>
                    </Tr>
                    <Tr>
                        <Td>Tipo da transação</Td>
                        <Td>{tableValues.transaction_type}</Td>
                    </Tr>
                </Tbody>
            </Table>
        }

        //Condicional que irá renderizar
        let propsData = this.props.data == null ? loading : tableContent

        return (
            <>
                <Col xl="12">
                    <Card>
                        <CardBody>
                            <div className="clearfix">
                                <h4 className="card-title mb-4">Payoff Long</h4>
                            </div>
                            <Row>
                                <Col lg="8">
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
                                <Col lg="4">
                                    <div className="table-rep-plugin">
                                        <div
                                            className="table-responsive mb-0"
                                            data-pattern="priority-columns"
                                        >
                                            {propsData}
                                        </div>
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