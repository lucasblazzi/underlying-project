import React, { Component } from "react";
import PropTypes from "prop-types";
import { Row, Col, Card, CardBody } from "reactstrap";
import { Table, Thead, Tbody, Tr, Td } from "react-super-responsive-table";
import ReactApexChart from "react-apexcharts";

class OptionsClose extends Component {
    constructor(props) {
        super(props);
        //console.log(this.props.data) 
        
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

        let tableContent;

        if (this.props.info != null) {
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
                        <Td>Nome</Td>
                        <Td>{this.props.info.name}</Td>
                    </Tr>
                    <Tr>
                        <Td>Tipo</Td>
                        <Td>{this.props.info.type}</Td>
                    </Tr>
                    <Tr>
                        <Td>Preço de exercício</Td>
                        <Td>{this.props.info.exercise_price}</Td>
                    </Tr>
                    <Tr>
                        <Td>Moeda</Td>
                        <Td>{this.props.info.currency}</Td>
                    </Tr>
                    <Tr>
                        <Td>Vencimento</Td>
                        <Td>{this.props.info.expiration_date}</Td>
                    </Tr>
                    <Tr>
                        <Td>Ativo base</Td>
                        <Td>{this.props.info.name_underlying}</Td>
                    </Tr>
                    <Tr>
                        <Td>Vencimento (em anos)</Td>
                        <Td>{this.props.info.expiration_time}</Td>
                    </Tr>
                </Tbody>
            </Table>
        }

        //Condicional que irá renderizar
        let propsInfo = this.props.info == null ? loading : tableContent

        this.state = {
            series: [
                {
                    name: "Valor",
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
            table: propsInfo
        }  
    }

    render() {
        return (
            <>
                <Col xl="12">
                    <Card>
                        <CardBody>
                            <div className="clearfix">
                                <h4 className="card-title mb-4">Preço de fechamento</h4>
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
                                            {this.state.table}
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
    info: PropTypes.object,
}

export default OptionsClose;