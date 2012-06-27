class Cell
  attr_accessor :id, :type, :status
  def initialize(id, type, status = nil)
    @id, @type, @status = id, type, status
    return self
  end
end

class Status
  attr_accessor :open, :reading
  def initialize(open=false, reading=0)

    @open, @reading = open, reading
  end
end

