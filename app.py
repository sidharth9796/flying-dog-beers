import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import os

df = pd.read_csv('https://raw.githubusercontent.com/sidharth9796/flying-dog-beers/master/BERT_metrics_analysis.csv')
df_count=pd.read_csv('https://raw.githubusercontent.com/sidharth9796/flying-dog-beers/master/entity_count.csv')

df1 = pd.read_csv('https://raw.githubusercontent.com/sidharth9796/flying-dog-beers/master/entity_count.csv')
df2 = pd.read_csv('https://raw.githubusercontent.com/sidharth9796/flying-dog-beers/master/data_new.csv')

df_model=pd.read_csv('https://raw.githubusercontent.com/sidharth9796/flying-dog-beers/master/datarecords.csv')
#df_summary=pd.read_csv('model_summary.csv')

external_stylesheets=[
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    {   'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
        'crossorigin': 'anonymous'},
         dbc.themes.BOOTSTRAP  ]

app = dash.Dash(__name__,external_stylesheets=external_stylesheets,suppress_callback_exceptions = True)
# app = dash.Dash(__name__)
#app = dash.Dash(__name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}])
#app = dash.Dash()
#assets_external_path='https://codepen.io/amyoshino/pen/jzXypZ.css/
#app.scripts.append_script('https://codepen.io/amyoshino/pen/jzXypZ.css')
#app.scripts.config.serve_locally = False
#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#'color': 'blue', 'fontSize': 14
#app.css.append_css({'external_url': 'https://codepen.io/amyoshino/pen/jzXypZ.css'})
model_summary_dataset=html.Div( [
              html.H1(children='Model summary with varying dataset',style={"margin-left":"4%",'fontSize':'3.0rem','font-family': 'Trocchi, serif','color':'blue'}),
              dcc.Dropdown(id="switches-inline-input-dataset-summary",
            options=[{
                    'label':i,
                    'value':i}for i in df['Total_Records'].unique()],
            placeholder="Select entity",
            style={'height': '300%', 'width': '100%','fontSize':'1.7rem'},
            value=[] ),

 dcc.Dropdown(id="switches-inline-input-metrics-summary",
            options= [  {'label':'BERT model' , 'value':'A-BERT'      },
                        {'label':'SPACY model' , 'value':'B-SPACY'    },
                     ],
          placeholder="Select entity",
          style={'height': '300%', 'width': '100%','fontSize':'1.7rem'},
          value=[] ) ,

dcc.Graph(id='model_dataset_graph',animate=True,style={"backgroundColor": "#1a2d46",'color':'#ffffff'} )
                            ] )

DropdownApp_entity_data =  html.Div([
    html.H1(children='Evaluation metrics',style={"margin-left":"4%",'fontSize':'3.0rem','font-family': 'Trocchi, serif','color':'blue'}),
    dcc.Dropdown(id="entity_dropdown_dataset_model",
                options=[{
                        'label': i,
                        'value': i}for i in df['Total_Records'].unique()],
                        placeholder="Select entity",
                        style={'height': '300%', 'width': '100%','fontSize':'1.7rem'},
                        value=[]),

    dbc.FormGroup(                                   [
            dbc.Label("Toggle Metrics",style={'fontSize':'2rem'},),
            dbc.Checklist(
                options=[
                    {"label": "Precision", "value": 'Precision'},
                    {"label": "Recall", "value":  'Recall'},
                    {"label": "F1", "value": 'F1'}
                ],
                value=[],
                id="switches-inline-input-modal-dataset",
                style={'height': '300%', 'width': '100%','fontSize':'1.7rem'},
                inline=True,
                switch=True,
            ),
        ]
    )  ,
    dcc.Graph(id='entity_graph_modal_dataset',animate=True,style={"backgroundColor": "#1a2d46",'color':'#ffffff'} ) ])

DropdownApp_entity = html.Div([
    html.H1(children='Evaluation metrics',style={"margin-left":"4%",'fontSize':'3.0rem','font-family': 'Trocchi, serif','color':'blue'}),
    dcc.Dropdown(id="entity_dropdown",
                options=[{
                        'label': i,
                        'value': i}for i in df['Entity'].unique()],
                        placeholder="Select entity",
                        style={'height': '300%', 'width': '100%','fontSize':'1.7rem'},
                        multi = True,
                        value=[]),

    dbc.FormGroup(                                   [
            dbc.Label("Toggle Metrics",style={'fontSize':'2rem'}),
            dbc.Checklist(
                options=[
                    {"label": "Precision", "value": 'Precision'},
                    {"label": "Recall", "value":  'Recall'},
                    {"label": "F1", "value": 'F1'}
                ],
                value=[],
                id="switches-inline-input-modal",
                inline=True,
                switch=True,
            ),
        ]
    )  ,
dcc.Graph(id='entity_graph',animate=True,style={"backgroundColor": "#1a2d46",'color':'#ffffff'} ) ])

DropdownApp_model= html.Div([
  html.H1(children='Model Summary',style={"margin-left":"4%",'fontSize':'3.0rem','font-family': 'Trocchi, serif','color':'blue'}),
  dcc.Dropdown(
              id="model_name",
              options=[{'label':"Model A",'value':"Model A"},
                      {"label":"Model B","value":"Model B"}  ],
                      placeholder="Select model",
              style={'height':'300%','width':'100%','fontSize':'2.0rem'},
              multi = True,
              value=[]),
  dcc.Graph(id='model_summary',animate=True,style={"backgroundColor": "#1a2d46",'color':'#ffffff'} ),
                            ])

DropdownApp_model_dataset= html.Div([
  html.H1(children='Model with varying dataset',style={"margin-left":"4%",'fontSize':'3.0rem','font-family': 'Trocchi, serif','color':'blue'}),
    dcc.Slider(
          id='dataset-slider',
          min=df['Total_Records'].min(),
          max=df['Total_Records'].max(),
          value=df['Total_Records'].max(),
          marks={str(Total_Records): str(Total_Records) for Total_Records in df['Total_Records'].unique()},
          step=None
      ),
  dcc.Graph(id='model_dataset_graph',animate=True,style={"backgroundColor": "#1a2d46",'color':'#ffffff'} )
                            ])


DropdownApp_model_summary_dataset=html.Div( [
  html.H1(children='Model summary with varying dataset',style={"margin-left":"4%",'fontSize':'3.0rem','font-family': 'Trocchi, serif','color':'blue'}),
  dcc.Dropdown(id="switches-inline-input-dataset-summary",
            options=[{
                    'label':i,
                    'value':i}for i in df['Total_Records'].unique()],
            placeholder="Select entity",
            style={'height': '300%', 'width': '100%','fontSize':'1.7rem'},
            value=[] ),

 dcc.Dropdown(id="switches-inline-input-metrics-summary",
            options= [  {'label':'BERT model' , 'value':'A-BERT'      },
                        {'label':'SPACY model' , 'value':'B-SPACY'    },
                     ],
          placeholder="Select entity",
          style={'height': '300%', 'width': '100%','fontSize':'1.7rem'},
          value=[] ) ,

dcc.Graph(id='model_dataset_graph',animate=True,style={"backgroundColor": "#1a2d46",'color':'#ffffff'} )
                            ] )

DropdownApp_model_term= html.Div([
    html.H2(children="ENTITY SUMMARY", style={"margin-left": "4%",'fontSize':'3.0rem','font-family': 'Trocchi, serif','color':'blue'}),
    dcc.Graph(
        id='dcc_entity',
        figure={
        'data':[go.Bar(x=df1['Entities'],
                y=df1['#Count'])],
         'layout':go.Layout(title='Tag Frequency',
                               colorway=["#EF963B", "#EF533B"],hovermode="closest",
                                xaxis={'title': "ENTITIES",
                                       'titlefont':{'color': 'black','size': 20},
                                       'tickfont':{'color': 'black','size': 12 } },
                               yaxis={'title': "TERM FREQUENCY",
                                      'titlefont':{'color': 'black','size': 20},
                                      'tickfont':{'color': 'black','size': 15 } },
                               legend={'x': 1, 'y':1 } ) } )
                                   ])


app.layout = html.Div(
    html.Div([
        html.Div(
            [  html.H1(children='Model Training Viewer',style={"margin-left": "10%",'fontSize':'4.5rem', 'font-family': 'Trocchi, serif' ,'color':'blue'},
                        className='six columns'),
                html.Div(children='''
                        Dash: A web application framework for Python.
                        ''',style={"margin-left": "10%",'fontSize':'2.5rem','color':'black'},
                        className='six columns'
                )
            ], className="row",style={"margin": "38px 40px"}
        ),
        html.Div(
        [      html.Div(
            [  html.Div([
                          dbc.Card(
                               [
                    #dbc.CardImg(src="logo.png", top=True),
                    dbc.CardBody(
                        [   html.Div([
                            html.H2(children="BERT METRICS ANALYSIS", style={"margin-left": "4%",'fontSize':'2.5rem','font-family':'Trocchi, serif','color':'blue',},className="card-title"),
                            dcc.Dropdown(id="entity_dropdown_front",
                                                    options=[{
                                                            'label':i,
                                                            'value':i}for i in df['Entity'].unique()],
                                                                        placeholder="Select entity",
                                                        style={'height': '300%', 'width': '100%'},
                                                        multi = True,
                                                        value=['ActionTaken'] ),
                            dbc.FormGroup([
                                    dbc.Label("Metrics",style={'fontSize':'2rem'},),
                                    dbc.Checklist(
                                        options=[
                                            {"label": "Precision", "value":'Precision'},
                                            {"label": "Recall", "value":'Recall'},
                                            {"label": "F1", "value":'F1'}
                                        ],
                                        value=[],
                                        id="switches-inline-input",
                                        style={'height': '300%', 'width': '100%','fontSize':'1.7rem'},
                                        inline=True,
                                        switch=True,
                                    ),
                                ]
                            ),
                            dcc.Graph(id='entity_graph_front',animate=True, style={'width': '100%'})  ,

                            html.P(
                                children="ENTITIES - Precision, F1, Recall scores ",style={"margin-left": "4%",'fontSize':'1.5rem','color':'blue'},
                                className="card-text",
                            ),
                            dbc.Button("Open App", id="openone",  color='warning', style={'margin': 'auto', 'width': '100%'}),
                            dbc.Modal(
                                [
                                    dbc.ModalBody(DropdownApp_entity),
                                    dbc.ModalFooter(
                                        dbc.Button("Close", id="closeone", className="ml-auto",outline=True,color="danger",block=True)
                                    ),
                                ],
                                id="modalone",size="xl"
                            ),
                        ]
                    ),
                ],
                style={"width": "70rem","height":"70rem",'background-color':'rgb(176,196,222)'},
            )     ],className='six columns'),

            html.Div([  dbc.Card(
                             [  #dbc.CardImg(src="logo.png", top=True),
                                 dbc.CardBody(
                                     [   html.Div([
                                             html.H1(children="MODEL SUMMARY",style={"margin-left": "4%",'fontSize':'2.5rem','font-family': 'Trocchi, serif','color':'blue'},className="card-title"),
                                             dcc.Dropdown(
                                                        id="model_name_front",
                                                        options=[{
                                                                'label': "Model A",
                                                                'value': "Model A"},
                                                                {"label": "Model B","value": "Model B"}
                                                                ],
                                                                placeholder="Select model",
                                                        style={'height': '300%', 'width': '100%'},
                                                        multi = True,
                                                        value=['Model A']),
                                        dcc.Graph(id='model_summary_front',animate=True,style={'margin':'20px 0px'}          )  ]),
                                        html.P(
                                            children="The Consolidated Training Results summary of models have been plotted",style={"margin-left": "4%",'fontSize':'1.5rem','color':'red'},
                                            className="card-text",
                                        ),
                                        dbc.Button("Open App", id="opentwo", color='primary', style={'margin': 'auto', 'width': '100%', "margin":"30px 0px"}),
                                        dbc.Modal(
                                            [
                                            #    dbc.ModalHeader("Modal"),
                                                dbc.ModalBody(DropdownApp_model),
                                                dbc.ModalFooter(
                                                    dbc.Button("Close", id="closetwo", className="ml-auto",outline=True,color="danger",block=True)
                                                ),
                                            ],
                                            id="modaltwo",size="xl"
                                        ),
                                    ]
                                ),
                            ],
                            style={"width": "70rem","height":"70rem",'background-color':'rgb(176,196,222)' },
                        )  ],className='six columns')
                                                       ],className="row",style={"margin":"38px 40px"}  ),




html.Div(
    [  html.Div([
                  dbc.Card(
                       [
            #dbc.CardImg(src="logo.png", top=True),
            dbc.CardBody(
                [   html.Div([
                    html.H2(children="ENTITY SUMMARY", style={"margin-left": "4%",'fontSize':'2.5rem','font-family':'Trocchi, serif','color':'blue'}, className="card-title"),
                    html.Div([

                            dcc.Graph(
                                id='dcc_entity_bottom_left',
                                figure={
                                'data':[go.Bar(x=df1['Entities'],
                                        y=df1['#Count'])],
                                 'layout':go.Layout(title='Tag Frequency',
                                                       colorway=["#EF963B", "#EF533B"],hovermode="closest",
                                                        xaxis={'title': "ENTITIES",
                                                               'titlefont':{'color': 'black','size': 20},
                                                               'tickfont':{'color': 'black','size': 12 } },
                                                       yaxis={'title': "TERM FREQUENCY",
                                                              'titlefont':{'color': 'black','size': 20},
                                                              'tickfont':{'color': 'black','size': 15 } },
                                                       legend={'x': 1, 'y':1 } ) } ,style={'width': '100%','margin-top': '82px'})


                    ]   )

                                                   ]),

                    html.P(
                        children="Entity Count ",style={"margin-left": "4%",'fontSize':'1.5rem','color':'blue',"margin-bottom": "7%"},
                        className="card-text",
                    ),
                    dbc.Button("Open App", id="openthree",  color='warning', style={'margin': 'auto', 'width': '100%'}),
                    dbc.Modal(
                        [
                            dbc.ModalBody(DropdownApp_model_term),
                            dbc.ModalFooter(
                                dbc.Button("Close", id="closethree", className="ml-auto",outline=True,color="danger",block=True)
                            ),
                        ],
                        id="modalthree",size="xl"
                    ),
                ]
            ),
        ],
        style={"width": "70rem",  "height":"74rem"       , 'background-color':'rgb(176,196,222)'},
    )     ],className='six columns'),

    html.Div([
                dbc.Card( [
                    #dbc.CardImg(src="logo.png", top=True),
                    dbc.CardBody(
                        [   html.Div([
                            html.H2(children="MODEL SUMMARY BASED ON RECORDS", style={"margin-left": "4%",'fontSize':'2.5rem',"font-weight":"bold",'font-family':'Trocchi, serif','color':'rgb(0,0,128)'}, className="card-title"),


                            html.P(
                            children="Select Option - DATASPLIT / METRICS ",style={"margin-left": "0%",'fontSize':'1.5rem', "font-weight":"bold", 'font-family':'Trocchi, serif','color':'rgb(47,79,79)'},className="card-title"),

                            dcc.Dropdown( id="radioitems-input",
                                       options=[
                                        { "label": " METRICS-Precision,Recall,F1 " , "value":"no"  },
                                        { "label": " DATA SPLIT-Train,Val,Test " , "value":"data_split"  }
                                                                                                                ],
                                       placeholder="Select option - DATASPLIT/METRICS ",
                                       style={'height': '300%', 'width': '100%','fontSize':'1.7rem'},
                                       value=[] )  ,
                           html.Div([
                             html.Div([
                            html.P(
                                children="Select Records",style={"margin-left": "0%",'fontSize':'1.5rem', "font-weight":"bold" , "margin-left": "4%",'font-family':'Trocchi, serif','color':'rgb(47,79,79)'},className="card-title"),
                             dcc.Dropdown( id="switches-inline-input-dataset-summary-front",
                                        options=[{
                                                'label':i,
                                                'value':i}for i in df_model['TOTAL RECORDS'].unique()],
                                        placeholder="Select DATASET - first",
                                        style={'height': '300%', 'width': '100%','fontSize':'1.7rem',"margin-left": "2%"},
                                        value=[] )  ] ,className='six columns' )  ,

                            html.Div([
                            html.P(
                                children="Select Model ",style={"margin-left": "0%",'fontSize':'1.5rem',"font-weight":"bold" , 'font-family':'Trocchi, serif','color':'rgb(47,79,79)'},className="card-title"),
                            dcc.Dropdown( id="switches-inline-input-modal-summary-front",
                                         options=[{
                                                 'label':i,
                                                 'value':i}for i in df_model['MODEL'].unique()],
                                          placeholder="Select MODEL - second",
                                          style={'height': '300%', 'width': '100%','fontSize':'1.7rem'},
                                          multi = True,
                                          value=[] )
                                                ], className='six columns')
                                          ]  , className="row" ) ,


                            dcc.Graph(id='model_summary_dataset-front',animate=True, style={'width': '100%','margin-top': '22px'} )
                                        ] ),
                            html.P(
                                children="RECORDS ",style={"margin-left": "4%",'fontSize':'1.5rem','color':'blue',"margin-bottom": "0%"},
                                className="card-text",
                            ),
                            dbc.Button("Open App", id="openfour",  color='primary', style={'margin': '0px', 'width': '100%'}),
                            dbc.Modal(
                                [   dbc.ModalBody(model_summary_dataset),
                                    dbc.ModalFooter(
                                    dbc.Button("Close", id="closefour", className="ml-auto",outline=True,color="danger",block=True)
                                    ),
                                ],
                                id="modalfour",size="xl"
                            ),
                        ]
                    ),
                ],
                style={"width": "70rem",'background-color':'rgb(176,196,222)'},
            )     ],className='six columns'),
                                           ], className="row",  style={"margin": "38px 40px"}       )  ,

            html.Div(
            [
                dbc.Card(
                        [
                        #dbc.CardImg(src="logo.png", top=True),
                        dbc.CardBody(
                            [   html.Div([
                                html.H2(children="BERT METRICS ANALYSIS", style={"margin-left": "0%",'fontSize':'2.5rem','font-family':'Trocchi, serif','color':'blue'},className="card-title"),
                                dcc.Dropdown(id="entity_dropdown_2",
                                                        options=[{
                                                                'label':i,
                                                                'value':i}for i in df['Entity'].unique()],
                                                                            placeholder="Select entity",
                                                            style={'height': '300%', 'width': '100%'},
                                                            multi = True,
                                                            value=['ActionTaken','Dosage'] ),
                                html.Div([
                                html.P(
                                    children="RECORDS ",style={"margin-left": "0%",'fontSize':'2.5rem','font-family':'Trocchi, serif','color':'blue'},className="card-title"),


                                html.Div(
                                dcc.Dropdown(id="entity_dropdown_dataset",
                                                        options=[{
                                                                'label':i,
                                                                'value':i}for i in df['Total_Records'].unique()],
                                                            placeholder="Select entity",
                                                            style={'height': '300%', 'width': '100%'},
                                                            value=['ActionTaken','Dosage'] ) ,className='four columns'  ,   style={"margin": "9px 0px"}    ),

                            #    html.P(
                            #        children="METRICS ",style={"margin": "18px 18px",'fontSize':'1.5rem','color':'blue',"font-weight":"bold"},
                            #        className="card-text",
                            #    ),
                                html.Div(
                                dbc.FormGroup([
                                        dbc.Checklist(
                                            options=[
                                                {"label": "Precision", "value":'Precision'},
                                                {"label": "Recall", "value":'Recall'},
                                                {"label": "F1", "value":'F1'}
                                            ],
                                            value=[],
                                            id="switches-inline-input-dataset",
                                            style={'height': '300%', 'width': '100%','fontSize':'1.7rem'},
                                            inline=True,
                                            switch=True,
                                        ),
                                    ]
                                )  ,className='six columns' , style={"margin": "9px 18px"}   ) ], className="row"    ),

                                dcc.Graph(id='entity_graph_front_dataset',animate=True, style={'width': '100%'})  ,
                                html.P(
                                    children="ENTITIES - Precision, F1, Recall scores based on varying RECORDS ",style={"margin-left": "4%",'fontSize':'1.5rem','color':'blue'},
                                    className="card-text",
                                ),
                                dbc.Button("Open App", id="openfive",color='warning', style={'margin':'20px','width':'90%'}),
                                dbc.Modal(
                                    [   dbc.ModalBody(DropdownApp_entity_data),
                                        dbc.ModalFooter(
                                            dbc.Button("Close", id="closefive", className="ml-auto",outline=True,color="danger",block=True)
                                        ),
                                    ],
                                    id="modalfive",size="xl"
                                ),
                            ]
                        ),
                    ],
                    style={"width": "145rem","height":"75rem",'background-color':'rgb(176,196,222)'},
                )     ],className='twelve columns')       ], className="row",  style={"margin": "38px 40px"}  )

                ]) ], className='ten columns offset-by-one')],
), style={"background-color": "rgb(220,220,220)"})



colors=['rgb(100,149,237)','rgb(55, 83, 109)','rgb(135,206,250)','rgb(192,192,192)','rgb(245,222,179)','rgb(255,228,225)','rgb(188,143,143)','rgb(128,128,128)','rgb(65,105,225)','rgb(244,164,96)','rgb(0,128,128)','rgb(152,251,152)','rgb(220,20,60)','rgb(255,140,0)','rgb(107,142,35)','rgb(221,160,221)','rgb(244,164,96)','rgb(128,0,0)','rgb(250,250,210)','rgb(245,255,250)']



#CARD 5
@app.callback(
    dash.dependencies.Output('entity_graph_front_dataset','figure'),
    [
    dash.dependencies.Input('switches-inline-input-dataset','value'),
    dash.dependencies.Input('entity_dropdown_dataset','value'),
    dash.dependencies.Input('entity_dropdown_2','value'),
    ] )
def update_figure(toggle_d,dropdown_d,entity_d):
    print("\n\n\n\n\n\n")
    print(toggle_d)
    print("\n\n\n\n\n\n")
#   print(type(dropdown))
    print(dropdown_d)
    data_select=[]
    total_df = df.groupby('Total_Records')

    for n,g in total_df:
        if n == dropdown_d:
            #print(min_df[i])df
            g=df[df['Total_Records'] == dropdown_d]
            print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print(g)
            #x=g[g['Entity'] == value]['Total_Records']
            for j in toggle_d:
                for index,value in enumerate(entity_d):
                    data_select.append(go.Bar(x=g['Total_Records'] ,y=g[g['Entity'] == value][j],text=("{0} {1}".format(value,j)),name=("{0} {1}".format(value,j)),textposition='auto',marker=dict(color = colors[index] ,line=dict(color='rgb(8,48,107)'))))
    print(data_select)
    print("-----------------------------------------------------")
    figure=dict(
            data=data_select,
            layout=go.Layout(title='EVALUATION METRICS',
                               colorway=["#EF963B", "#EF533B"],hovermode="closest",
                                xaxis={'title': "Records",
                                       'titlefont':{'color': 'black','size': 20},
                                       'tickfont':{'color': 'black','size': 20 } },
                               yaxis={'title': "ACCURACY",
                                      'titlefont':{'color': 'black','size': 20},
                                      'tickfont':{'color': 'black','size': 20 } },
                               legend={'x': 1, 'y':1 }
                                       )
                                      )
    return figure

#CARD 1 BERT METRICS ANALYSIS
@app.callback(
    dash.dependencies.Output('entity_graph_front','figure'),
    [dash.dependencies.Input('entity_dropdown_front','value'),
    dash.dependencies.Input('switches-inline-input','value'),
            ]   )


def update_figure(dropdown,toggle):
    print("\n\n\n\n\n\n")
    print(toggle)
    print("\n\n\n\n\n\n")
#   print(type(dropdown))
    print(len(dropdown))
    print(dropdown)
    data_select=[]

    for j in toggle:
        for index,value in enumerate(dropdown):
            data_select.append(go.Bar(x=df[df['Entity'] == value]['Total_Records'],y=df[df['Entity'] == value][j],text=("{0} {1}".format(value,j)),name=("{0} {1}".format(value,j)),textposition='auto',marker=dict(color = colors[index] ,line=dict(color='rgb(8,48,107)'))))
    print(data_select)

    print("-----------------------------------------------------")

    figure=dict(
            data=data_select,
            layout=go.Layout(title='EVALUATION METRICS',
                               colorway=["#EF963B", "#EF533B"],hovermode="closest",
                                xaxis={'title': "RECORDS",
                                       'titlefont':{'color': 'black','size': 20},
                                       'tickfont':{'color': 'black','size': 20 } },
                               yaxis={'title': "ACCURACY",
                                      'titlefont':{'color': 'black','size': 20},
                                      'tickfont':{'color': 'black','size': 20 } },
                               legend={'x': 1, 'y':1 }
                                       )
                                      )
    return figure

#card four - MODEL SUMMARY BASED ON RECORDS
@app.callback(
    dash.dependencies.Output('model_summary_dataset-front','figure'),
    [
    dash.dependencies.Input('switches-inline-input-dataset-summary-front','value'),
    dash.dependencies.Input('switches-inline-input-modal-summary-front','value'),
    dash.dependencies.Input('radioitems-input','value'),
                          ] )

def modelsummarydatasetfront(dataset,model,split):
    print(split)
    print("njnkbttttttttttttttttttttttttt")
    print("\n\n\n\n\n\n")
    print("\n\n\n\n\n\n")
    #print(type(dropdown))
    print(dataset)
    data_select=[]
    metrics=['Precision','Recall','F1']
    split_list=['TRAIN','VAL','TEST']
    total_df =df_model.groupby('TOTAL RECORDS')
    for n,g in total_df:
        if n == dataset:
            #print(min_df[i])df
            g=df_model[df_model['TOTAL RECORDS'] == dataset]
            print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print(g)
            #x=g[g['Entity'] == value]['Total_Records']
            if split=='data_split':
                print("yessssssssssssssssssssssssssssssssssssssssssssssssssssssss")
                for i in split_list:
                    for index,value in enumerate(model):
                        data_select.append(go.Bar(x=g['TOTAL RECORDS'] ,y=g[g['MODEL'] == value][i],text=("{0} {1}".format(value,i)),name=("{0} {1}".format(value,i)),textposition='auto',marker=dict(color = colors[index] ,line=dict(color='rgb(8,48,107)'))))

            elif split=='no':
                for j in metrics:
                    for index,value in enumerate(model):
                        data_select.append(go.Bar(x=g['TOTAL RECORDS'] ,y=g[g['MODEL'] == value][j],text=("{0} {1}".format(value,j)),name=("{0} {1}".format(value,j)),textposition='auto',marker=dict(color = colors[index] ,line=dict(color='rgb(8,48,107)'))))


    figure=dict(
                            data=data_select,
                            layout=go.Layout(title='EVALUATION METRICS',
                                   colorway=["#EF963B", "#EF533B"],hovermode="closest",
                                    xaxis={'title': "Records",
                                           'titlefont':{'color': 'black','size': 20},
                                           'tickfont':{'color': 'black','size': 20 } },
                                   yaxis={'title': "ACCURACY",
                                          'titlefont':{'color': 'black','size': 20},
                                          'tickfont':{'color': 'black','size': 20 } },
                                   legend={'x': 1, 'y':1 }
                                           )
                                          )
    return figure


#CARD 2 - MODEL SUMMARY
@app.callback(
    dash.dependencies.Output('model_summary_front','figure'),
    [dash.dependencies.Input('model_name_front','value')])
def model_sum(model_name):
    print(model_name)
    data_model=[]
    for index,value in enumerate(model_name):
        data_model.append(go.Bar(x=df2['Results'],y=df2[value],text=df2[value],name=value,textposition='auto',marker=dict(color=colors[index],line=dict(color='rgb(8,48,107)'))))
    model_figure=dict(
            data=data_model,
            layout=go.Layout(title='Model Summary',
                               colorway=["#EF963B", "#EF533B"],hovermode="closest",
                                xaxis={'title': "METRICS",
                                       'titlefont':{'color': 'black','size': 20},
                                       'tickfont':{'color': 'black','size': 20 } },
                               yaxis={'title': "ACCURACY",
                                      'titlefont':{'color': 'black','size': 20},
                                      'tickfont':{'color': 'black','size': 20 } },
                               legend={'x': 1, 'y':1 }
                                       )
                                      )
    return model_figure


#CARD 3 - modal card one - BERT METRICS ANALYSIS

@app.callback(
    dash.dependencies.Output('entity_graph','figure'),
    [ dash.dependencies.Input('entity_dropdown','value'),
      dash.dependencies.Input('switches-inline-input-modal','value')

     ])
def update_figure(dropdown,toggle):
#   print(type(dropdown))
    print(len(dropdown))
    print(dropdown)
    data_select=[]
    for j in toggle:
        for index,value in enumerate(dropdown):
            data_select.append(go.Bar(x=df[df['Entity'] == value]['Total_Records'],y=df[df['Entity'] == value][j],text=("{0} {1}".format(value,j)),name=("{0} {1}".format(value,j)),textposition='auto',marker=dict(color = colors[index] ,line=dict(color='rgb(8,48,107)'))))
    print(data_select)

    print("-----------------------------------------------------")
    figure=dict(
            data=data_select,
            layout=go.Layout(title='EVALUATION METRICS',height=850,
                               colorway=["#EF963B", "#EF533B"],hovermode="closest",
                                xaxis={'title': "DATASET_RANGE",
                                       'titlefont':{'color': 'black','size': 20},
                                       'tickfont':{'color': 'black','size': 20 },
                                      },
                               yaxis={'title': "ACCURACY",
                                      'titlefont':{'color':'black','size': 20},
                                      'tickfont':{'color':'black','size': 20 }
                                      },

                                ) )
    return figure


#CARD 2 MODAL MODEL SUMMARY
@app.callback(
    dash.dependencies.Output('model_summary','figure'),
    [dash.dependencies.Input('model_name','value')])
def model_sum(model_name):
    print(model_name)
    data_model=[]
    for index,value in enumerate(model_name):
        data_model.append(go.Bar(x=df2['Results'],y=df2[value],text=df2[value],name=value,textposition='auto',marker=dict(color=colors[index],line=dict(color='rgb(8,48,107)'))))

    model_figure=dict(
    data=data_model,
    layout=go.Layout(title='Model Summary',height=850,
                               colorway=["#EF963B", "#EF533B"],hovermode="closest",
                                xaxis={'title': "METRICS",
                                       'titlefont':{'color':'black','size':20},
                                       'tickfont':{'color':'black','size':20 } },
                               yaxis={'title': "ACCURACY",
                                      'titlefont':{'color': 'black','size':20},
                                      'tickfont':{'color': 'black','size':20 } },
                               legend={'x':1,'y':1}
                                       ) )
    return model_figure



#Module one
@app.callback(
    dash.dependencies.Output("modalone", "is_open"),
    [dash.dependencies.Input("openone", "n_clicks"), dash.dependencies.Input("closeone", "n_clicks")],
    [dash.dependencies.State("modalone", "is_open")],
)
def toggle_modal(n1,n2,is_open):
    if n1 or n2:
        return not is_open
    return is_open

#Module Two
@app.callback(
    dash.dependencies.Output("modaltwo","is_open"),
    [dash.dependencies.Input("opentwo","n_clicks"), dash.dependencies.Input("closetwo","n_clicks")],
    [dash.dependencies.State("modaltwo","is_open")],
)
def toggle_modal(n1,n2,is_open):
    if n1 or n2:
        return not is_open
    return is_open

#Module Three
@app.callback(
    dash.dependencies.Output("modalthree","is_open"),
    [dash.dependencies.Input("openthree","n_clicks"), dash.dependencies.Input("closethree","n_clicks")],
    [dash.dependencies.State("modalthree","is_open")],
)
def toggle_modal(n1,n2,is_open):
    if n1 or n2:
        return not is_open
    return is_open

#Module four
@app.callback(
    dash.dependencies.Output("modalfour","is_open"),
    [dash.dependencies.Input("openfour","n_clicks"),
    dash.dependencies.Input("closefour","n_clicks")],
    [dash.dependencies.State("modalfour","is_open")],
)
def toggle_modal(n1,n2,is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    dash.dependencies.Output("modalfive","is_open"),
    [dash.dependencies.Input("openfive","n_clicks"), dash.dependencies.Input("closefour","n_clicks")],
    [dash.dependencies.State("modalfive","is_open")],
)
def toggle_modal(n1,n2,is_open):
    if n1 or n2:
        return not is_open
    return is_open


if __name__ == '__main__':
    app.run_server(debug=True,port=8056)
