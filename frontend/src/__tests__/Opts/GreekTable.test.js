import React from 'react';
import GreekTable from '../../pages/Opts/GreekTable';
import renderer from 'react-test-renderer'

it('Página', () => {
    const tree = renderer.create(<div class = "clearfix"/>).toJSON();
    expect(tree).toMatchSnapshot();
})