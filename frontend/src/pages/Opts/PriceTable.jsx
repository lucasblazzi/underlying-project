import React, { Component } from "react";
import PropTypes from "prop-types";
import { Row, Col, Card, CardBody } from "reactstrap";
import { Table, Thead, Tbody, Tr, Th, Td } from "react-super-responsive-table";
import "react-super-responsive-table/dist/SuperResponsiveTableStyle.css";
import Loading from "components/CommonForBoth/Loading";

class PriceTable extends Component {
    constructor(props) {
        super(props);
        this.state = {};
    }

    render() {
        //Componente correto
        let tableRows;
        let loading = <Loading />;
        if (this.props.data != null) {
            tableRows = <Table
                id="price"
                className="table table-striped table-bordered"
            >
                <Thead>
                    <Tr>
                        <Th></Th>
                        <Th>Preço de abertura</Th>
                        <Th>Preço máximo</Th>
                        <Th>Preço mínimo</Th>
                        <Th>Preço médio</Th>
                        <Th>Preço de fechamento</Th>
                        <Th>Melhor preço de compra</Th>
                        <Th>Melhor preço de venda</Th>
                        <Th>Nº de transações</Th>
                        <Th>Quantidade de papéis negociados</Th>
                        <Th>Volume financeiro negociado</Th>
                    </Tr>
                </Thead>
                <Tbody>
                    <Tr>
                        <Td>Valor</Td>
                        {this.props.data.map((e, index) => (
                            index == 9 
                                ? <Td key={index}>R${e.value}</Td>
                                : <Td key={index}>{e.value}</Td>
                        ))}

                    </Tr>
                </Tbody>
            </Table>
        }

        //Condicional que irá renderizar
        let propsData = this.props.data == null ? loading : tableRows
        return (
            <>
                <Col xl="12">
                    <Card>
                        <CardBody>
                            <div className="clearfix">
                                <h4 className="card-title mb-4">Informações de mercado</h4>
                            </div>
                            <Row>
                                <Col lg="12">
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

PriceTable.propTypes = {
    data: PropTypes.array,
}

export default PriceTable;