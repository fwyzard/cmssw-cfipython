import FWCore.ParameterSet.Config as cms

Chi2MeasurementEstimator = cms.ESProducer('Chi2MeasurementEstimatorESProducer',
  ComponentName = cms.string('Chi2'),
  MaxChi2 = cms.double(30),
  nSigma = cms.double(3),
  MaxDispacement = cms.double(0.5),
  MaxSagitta = cms.double(2),
  MinimalTolerance = cms.double(0.5),
  appendToDataLabel = cms.string('')
)
